#!/usr/bin/env python3
"""Daily Study Reminder — fires Mon-Fri 5:45 PM CDT via GitHub Actions."""
import json, os, requests
from datetime import date, datetime

BOT_TOKEN  = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID    = os.environ["TELEGRAM_CHAT_ID"]
API_URL    = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
START_DATE = date(2026, 3, 23)

DAY_MAP = {
    0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"
}

def send(text):
    r = requests.post(API_URL, json={"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML", "disable_web_page_preview": True})
    r.raise_for_status()
    return r.status_code

def get_week_day():
    today = date.today()
    delta = (today - START_DATE).days
    week_num  = (delta // 7) + 1
    day_short = DAY_MAP[today.weekday()]
    study_day = delta + 1
    return week_num, day_short, study_day

def load_roadmap():
    path = os.path.join(os.path.dirname(__file__), "../roadmap/weeks.json")
    with open(path) as f:
        return json.load(f)

def load_resources():
    path = os.path.join(os.path.dirname(__file__), "../roadmap/daily_resources")
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return {}

def find_resources(topic, resources):
    """Fuzzy match: find best resource entry by keyword overlap."""
    if not resources:
        return None
    topic_words = set(topic.lower().replace(",", "").replace(":", "").replace("(", "").replace(")", "").split())
    best_match = None
    best_score = 0
    for key, val in resources.items():
        key_words = set(key.lower().replace(",", "").replace(":", "").replace("(", "").replace(")", "").split())
        overlap = len(topic_words & key_words)
        if overlap > best_score:
            best_score = overlap
            best_match = val
    return best_match if best_score >= 2 else None

if __name__ == "__main__":
    weeks = load_roadmap()
    resources = load_resources()
    week_num, day_short, study_day = get_week_day()

    if week_num < 1 or week_num > len(weeks):
        send(f"Study bot active — outside {len(weeks)}-week window (week {week_num}).")
    else:
        week = weeks[week_num - 1]
        daily_focus = week.get("daily_focus", {})
        topic = daily_focus.get(day_short)

        if not topic:
            send(f"No task scheduled for {day_short} in Week {week_num}.")
        else:
            total_days = len(weeks) * 5
            filled = int((study_day / total_days) * 20)
            bar = chr(9608) * filled + chr(9617) * (20 - filled)
            pct = round((study_day / total_days) * 100, 1)

            # Find matching resources
            res = find_resources(topic, resources)

            # Build resource links section
            res_text = ""
            if res:
                res_text = "\n\U0001f4d6 <b>Learning Resources</b>\n"
                if "udemy" in res:
                    res_text += f"  \U0001f393 <b>Udemy:</b> {res['udemy']['course']}\n"
                    res_text += f"      Section: {res['udemy']['section']}\n"
                if "youtube" in res:
                    res_text += f"  \u25b6\ufe0f <b>YouTube:</b> <a href=\"{res['youtube']['url']}\">{res['youtube']['title']}</a>\n"
                if "article" in res:
                    res_text += f"  \U0001f4c4 <b>Article:</b> <a href=\"{res['article']['url']}\">{res['article']['title']}</a>\n"
            else:
                res_text = "\n\U0001f4d6 <i>No specific resources mapped — check official docs.</i>\n"

            # Week-level info
            lab_task = week.get("lab_task", "See daily focus above")
            project = week.get("project", "")
            github_goal = week.get("github_goal", "")
            cert_focus = week.get("cert_focus", "")

            msg = (
                f"\U0001f4da <b>DevOps Daily Reminder \u2014 {day_short}</b>\n"
                f"\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\n"
                f"\U0001f4c5 Week <b>{week_num}/{len(weeks)}</b> \u2014 {week.get('theme', '')}\n"
                f"\U0001f522 Day <b>{study_day}/{total_days}</b> | {cert_focus}\n"
                f"<code>{bar}</code> {pct}%\n\n"
                f"\U0001f3af <b>Today's Focus</b>\n"
                f"{topic}\n\n"
                f"\U0001f52c <b>Lab Task (this week)</b>\n"
                f"{lab_task}\n\n"
                f"\U0001f4c1 <b>Project</b>: {project}\n"
                f"\U0001f4be <b>GitHub Goal</b>: {github_goal}\n"
                f"{res_text}\n"
                f"\u23f1 <b>3-Hour Study Block</b>\n"
                f"\u2022 Hour 1 (0:00\u20141:00): Watch video + read docs from links above\n"
                f"\u2022 Hour 2 (1:00\u20142:30): Hands-on lab \u2014 complete the task\n"
                f"\u2022 Hour 3 (2:30\u20143:00): Write notes, commit to GitHub, review\n\n"
                f"\U0001f916 <i>devops-study-bot | {datetime.now().strftime('%Y-%m-%d')} | {pct}% complete</i>"
            )
            code = send(msg)
            print(f"Telegram {code} | Week {week_num} | {day_short} | Day {study_day}")
