# 🤖 DevOps Study Bot

> Automated Slack reminders for a 5-month DevOps mastery roadmap.
> Built by a Salesforce Developer transitioning to DevOps/SRE.
> Powered by GitHub Actions — zero servers, zero cost.

![Daily Reminder](https://img.shields.io/badge/Daily_Reminder-5%3A45_PM_CDT-blue)
![Weekly Review](https://img.shields.io/badge/Weekly_Review-Sunday_7PM-green)
![Exam Alerts](https://img.shields.io/badge/Exam_Alerts-3_Certifications-orange)

---

## 📅 Roadmap Timeline

| Milestone | Date | Status |
|---|---|---|
| 🚀 Start | March 23, 2026 | ✅ Active |
| 🏆 AWS SAA-C03 Exam | May 16, 2026 | ⏳ Upcoming |
| 🏆 Terraform Associate 004 | May 30, 2026 | ⏳ Upcoming |
| 🏆 CKA Exam | August 1, 2026 | ⏳ Upcoming |
| 🎯 Job-Ready Target | August 9, 2026 | ⏳ Upcoming |

---

## 🤖 Automated Tasks (6 GitHub Actions Workflows)

| # | Workflow | Schedule | Purpose |
|---|---|---|---|
| 1 | `daily_reminder.yml` | Mon–Fri 5:45 PM CDT | Today's exact study focus + 3-hr block breakdown |
| 2 | `weekly_review.yml` | Sunday 7:00 PM CDT | Full weekly review + self-assessment questions + scorecard |
| 3 | `exam_alert_aws.yml` | May 9 8:00 AM CDT (once) | 7-day AWS SAA final sprint plan + top topics + exam traps |
| 4 | `exam_alert_tf.yml` | May 23 8:00 AM CDT (once) | 7-day Terraform 004 final sprint plan + 004-specific topics |
| 5 | `exam_alert_cka.yml` | July 25 8:00 AM CDT (once) | 7-day CKA final sprint + killer.sh strategy + exam-day tips |
| 6 | `monthly_checkin.yml` | 23rd monthly 8:00 PM CDT | Skills checklist + GitHub portfolio + cert status + LinkedIn |

---

## ⚙️ Setup (5 minutes)

### Step 1 — Fork or clone this repo
```bash
git clone https://github.com/YOUR_USERNAME/devops-study-bot.git
cd devops-study-bot
```

### Step 2 — Create a Slack Incoming Webhook
1. Go to https://api.slack.com/apps
2. Click **Create New App** → **From scratch**
3. Name it `DevOps Study Bot`, select your workspace
4. Click **Incoming Webhooks** → toggle **On**
5. Click **Add New Webhook to Workspace** → select a channel (e.g., `#devops-study`)
6. Copy the webhook URL (starts with `https://hooks.slack.com/services/...`)

### Step 3 — Add GitHub Secret
1. Go to your GitHub repo → **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Name: `SLACK_WEBHOOK_URL`
4. Value: paste your Slack webhook URL
5. Click **Add secret**

### Step 4 — Enable GitHub Actions
1. Go to **Actions** tab in your repo
2. Click **Enable Actions**
3. All 6 workflows are now active and will run on their schedules

### Step 5 — Test immediately
```bash
# Trigger any workflow manually from the Actions tab
# Click workflow → Run workflow → Run workflow
```

---

## 📁 Repository Structure

```
devops-study-bot/
├── .github/
│   └── workflows/
│       ├── daily_reminder.yml      # Task 1: Mon–Fri 5:45 PM CDT
│       ├── weekly_review.yml       # Task 2: Sunday 7:00 PM CDT
│       ├── exam_alert_aws.yml      # Task 3: May 9 (AWS SAA alert)
│       ├── exam_alert_tf.yml       # Task 4: May 23 (Terraform alert)
│       ├── exam_alert_cka.yml      # Task 5: July 25 (CKA alert)
│       └── monthly_checkin.yml     # Task 6: 23rd monthly
├── scripts/
│   ├── daily_reminder.py           # Week-aware daily study focus
│   ├── weekly_review.py            # Weekly scorecard + self-assessment
│   ├── exam_alert.py               # Pre-exam sprint plan by cert name
│   └── monthly_checkin.py          # Monthly milestone review
├── roadmap/
│   └── weeks.json                  # All 20 weeks with daily tasks embedded
└── README.md
```

---

## 🔔 What Each Slack Message Contains

### Daily Reminder (5:45 PM weekdays)
- Today's exact topic (e.g., "Tuesday: Network Policies: podSelector, namespaceSelector")
- This week's lab task
- Certification focus for the week
- GitHub commit goal
- LinkedIn goal
- Your full 3-hour block breakdown (theory / lab / notes / quiz)
- Day X of 140 progress counter

### Weekly Review (Sunday 7 PM)
- Completion checklist for the week
- 5 self-assessment questions specific to this week's topics
- Scorecard template (theory / hands-on / GitHub / LinkedIn / cert prep)
- What to do if any score is below 7/10
- Preview of next week

### Exam Alerts (7 days before each exam)
- Day-by-day 7-day sprint plan
- Top 15 topics to drill
- Common exam traps to avoid
- Exam day checklist (ID, quiet room, internet, timing)

### Monthly Check-in (23rd of each month)
- Skills mastery checklist for the month
- GitHub portfolio projects expected to be live
- Certification status
- LinkedIn presence check
- On-track signal (what score/progress looks like at this point)

---

## 💡 Customization

To adjust a schedule, edit the `cron:` line in the workflow YAML.
[Cron reference → crontab.guru](https://crontab.guru)

To add a new reminder type, add a new `.py` script in `scripts/` and a new workflow in `.github/workflows/`.

---

## 🧠 Skills This Bot Itself Demonstrates

> This bot is also **Portfolio Project 0** — it shows:
> - GitHub Actions automation (scheduled workflows)
> - Python scripting (JSON data processing, HTTP requests)
> - Slack webhook integration
> - Config-driven design (roadmap/weeks.json drives all messages)
> - No servers, no cost, fully automated

---

*Built as part of a 5-month DevOps mastery roadmap. March → August 2026.*
