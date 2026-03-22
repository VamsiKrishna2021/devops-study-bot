#!/usr/bin/env python3
"""Daily Study Reminder — fires Mon-Fri 5:45 PM CDT via GitHub Actions."""
import json, os, requests
from datetime import date, datetime

BOT_TOKEN  = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID    = os.environ["TELEGRAM_CHAT_ID"]
API_URL    = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
START_DATE = date(2026, 3, 23)

def send(text):
    r = requests.post(API_URL, json={"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"})
    r.raise_for_status()
    return r.status_code

def get_week_day():
    today = date.today()
    delta = (today - START_DATE).days
    week_num  = (delta // 7) + 1
    day_names = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    day_name  = day_names[today.weekday()]
    study_day = delta + 1
    return week_num, day_name, study_day

def load_roadmap():
    path = os.path.join(os.path.dirname(__file__), "../roadmap/weeks.json")
    with open(path) as f:
        return json.load(f)

if __name__ == "__main__":
    roadmap = load_roadmap()
    week_num, day_name, study_day = get_week_day()
    weeks = roadmap["weeks"]

    if week_num < 1 or week_num > len(weeks):
        send(f"📅 Study bot active — outside 20-week window (week {week_num}).")
    else:
        week = weeks[week_num - 1]
        day  = week.get("days", {}).get(day_name)

        if not day:
            send(f"🌴 No task scheduled for {day_name} in Week {week_num}.")
        else:
            total  = 100
            filled = int((study_day / total) * 20)
            bar    = "█" * filled + "░" * (20 - filled)
            pct    = round((study_day / total) * 100, 1)

            msg = (
                f"📚 <b>DevOps Daily Reminder — {day_name}</b>\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
                f"📅 Week <b>{week_num}/20</b> — {week['theme']}\n"
                f"🔢 Day <b>{study_day}/100</b> | {week['cert_focus']}\n"
                f"<code>{bar}</code> {pct}%\n\n"
                f"🎯 <b>Today's Topic</b>\n"
                f"{day['topic']}\n\n"
                f"🔬 <b>Lab Task</b>\n"
                f"{day['lab']}\n\n"
                f"💾 <b>GitHub Commit Goal</b>\n"
                f"<code>{day['commit']}</code>\n\n"
                f"⏱ <b>3-Hour Study Block</b>\n"
                f"• Hour 1 (0:00–1:00): Read docs + watch 1 focused video\n"
                f"• Hour 2 (1:00–2:30): Hands-on lab — complete the task above\n"
                f"• Hour 3 (2:30–3:00): Write notes, commit to GitHub, review\n\n"
                f"🤖 <i>devops-study-bot | {datetime.now().strftime('%Y-%m-%d')} | {pct}% through the roadmap. Keep going.</i>"
            )
            code = send(msg)
            print(f"Telegram {code} | Week {week_num} | {day_name} | Day {study_day}")
