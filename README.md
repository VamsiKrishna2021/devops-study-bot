# 🤖 DevOps Study Bot (Telegram Edition)

> A self-running GitHub Actions bot that sends personalized DevOps study reminders,
> weekly reviews, exam sprint plans, and monthly check-ins **directly to your Telegram** — every day, automatically.

[![Daily Reminder](https://github.com/VamsiKrishna2021/devops-study-bot/actions/workflows/daily_reminder.yml/badge.svg)](https://github.com/VamsiKrishna2021/devops-study-bot/actions/workflows/daily_reminder.yml)
[![Weekly Review](https://github.com/VamsiKrishna2021/devops-study-bot/actions/workflows/weekly_review.yml/badge.svg)](https://github.com/VamsiKrishna2021/devops-study-bot/actions/workflows/weekly_review.yml)

---

## 📐 Architecture

GitHub Actions (CRON scheduler) → Python Scripts (week-aware logic) → Telegram Bot API → Your Telegram chat

**Zero cost. Zero third-party services. Just a Telegram bot token + GitHub secret.**

---

## ⚡ Automation Schedule

| Workflow | Schedule | What You Receive |
|---|---|---|
| **Daily Reminder** | Mon–Fri 5:45 PM CDT | Topic, lab task, commit goal, 3-hr block, day X/100 progress bar |
| **Weekly Review** | Sunday 7:00 PM CDT | 5 self-assessment questions, completion checklist, next week preview |
| **AWS SAA Alert** | May 9, 2026 (once) | 7-day sprint plan, top 15 topics, exam traps |
| **Terraform 004 Alert** | May 23, 2026 (once) | 7-day sprint plan, all 004-new topics, traps |
| **CKA Alert** | July 25, 2026 (once) | 7-day sprint, killer.sh strategy, kubectl speed tips |
| **Monthly Check-in** | 23rd monthly 8 PM CDT | Skills checklist, expected projects, cert status, LinkedIn milestone |

---

## 🚀 Setup

### 1. Create Telegram Bot
- Open Telegram → @BotFather → /newbot → copy the token

### 2. Get Chat ID
- Message your bot, then visit: `https://api.telegram.org/bot<TOKEN>/getUpdates`
- Copy the `"id"` inside `"chat"`

### 3. Add 2 GitHub Secrets
Repo → Settings → Secrets → Actions → New secret
- `TELEGRAM_BOT_TOKEN` → your token
- `TELEGRAM_CHAT_ID` → your chat id

### 4. Test
Actions tab → Daily Study Reminder → Run workflow

---

*Built by [@VamsiKrishna2021](https://github.com/VamsiKrishna2021) | Started March 2026*
