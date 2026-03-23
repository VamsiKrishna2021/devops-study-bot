#!/usr/bin/env python3
"""Weekly Review — fires Sunday 7 PM CDT via GitHub Actions."""
import json, os, requests
from datetime import date

BOT_TOKEN  = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID    = os.environ["TELEGRAM_CHAT_ID"]
API_URL    = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
START_DATE = date(2026, 3, 23)

def send(text):
    r = requests.post(API_URL, json={"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML", "disable_web_page_preview": True})
    r.raise_for_status()

def load_roadmap():
    path = os.path.join(os.path.dirname(__file__), "../roadmap/weeks.json")
    with open(path) as f:
        return json.load(f)

QUESTIONS = {
    1:  ["Can you explain the Linux permission model (rwx, octal, ACLs)?",
         "Write a bash for-loop that iterates over files and renames them.",
         "What is the difference between a systemd service and a cron job?",
         "How do you trace which process is listening on port 8080?",
         "Explain git rebase vs merge — when do you use each?"],
    2:  ["Explain Git internals: commits, staging, .gitignore.",
         "What is the difference between rebase and cherry-pick?",
         "How do branch protection rules work in GitHub?",
         "Write a bash function with error handling (set -e, trap).",
         "How do grep, sed, and awk differ for log parsing?"],
    3:  ["What is the difference between an IAM Role and an IAM User?",
         "Explain VPC subnets, route tables, and NAT Gateway.",
         "How do Security Groups differ from NACLs?",
         "Explain EC2 instance types and placement groups.",
         "What are S3 storage classes and lifecycle policies?"],
    4:  ["Explain RDS Multi-AZ vs Read Replica.",
         "How does an ALB route traffic differently than an NLB?",
         "What is CloudWatch vs CloudTrail vs Config?",
         "Explain Lambda cold starts and concurrency.",
         "When would you choose Fargate over ECS on EC2?"],
    5:  ["What happens in each layer of a Docker image build?",
         "Why use multi-stage builds? What problem do they solve?",
         "Explain Docker bridge networking.",
         "What is the difference between a volume and a bind mount?",
         "Write a docker-compose.yml with 3 services from memory."],
    6:  ["Explain Lambda triggers and API Gateway integration.",
         "What is ECS task definition vs service?",
         "How does Route 53 failover routing work?",
         "What is CloudFront OAC and why replace OAI?",
         "Explain SQS vs SNS vs EventBridge."],
    7:  ["Explain the AWS Shared Responsibility Model.",
         "Design a highly available web app architecture.",
         "What are the 6 pillars of the Well-Architected Framework?",
         "When do you use SQS vs SNS vs EventBridge?",
         "Walk through your SAA exam prep strategy."],
    8:  ["What is Terraform state and why is remote state important?",
         "Explain the difference between count and for_each.",
         "How do you structure a reusable Terraform module?",
         "What does terraform plan show that apply doesn't?",
         "What is a data source in Terraform?"],
    9:  ["Explain Terraform workspaces vs directory structure.",
         "What is Sentinel and how does it enforce policy-as-code?",
         "What are ephemeral resources in Terraform 004?",
         "How does VCS-driven workflow differ from CLI-driven?",
         "Write a terraform test block from memory."],
    10: ["Explain GitHub Actions: triggers, jobs, steps.",
         "What is OIDC and why better than static AWS credentials?",
         "How do multi-stage CI/CD pipelines work?",
         "What are GitHub Environments and approval gates?",
         "How do you deploy to ECS with GitHub Actions?"],
    11: ["Explain the Terraform core workflow: Write, Plan, Apply.",
         "What is the purpose of terraform.lock.hcl?",
         "How do you handle secrets in Terraform?",
         "What are the new features in Terraform 004 vs 003?",
         "Explain provider versioning and constraint syntax."],
    12: ["Name all K8s control plane components and what each does.",
         "What is the difference between a Deployment and a StatefulSet?",
         "Explain ClusterIP vs NodePort vs LoadBalancer services.",
         "How do you inject a Secret as env var in a Pod?",
         "Write kubectl create deployment with dry-run from memory."],
    13: ["What does a CNI plugin do in Kubernetes?",
         "Write a NetworkPolicy that allows only frontend to reach backend.",
         "Explain Ingress TLS termination.",
         "What is the relationship between PV, PVC, and StorageClass?",
         "How does CoreDNS resolve service names?"],
    14: ["Explain Role vs ClusterRole — when do you need each?",
         "What are Pod Security Standards (Restricted vs Baseline)?",
         "How does HPA decide when to scale?",
         "Walk through a kubeadm cluster upgrade step by step.",
         "A pod is in CrashLoopBackOff — what are your first 5 commands?"],
    15: ["Walk through an etcd backup and restore from memory.",
         "Explain nodeAffinity vs taints/tolerations.",
         "How do liveness vs readiness probes work?",
         "What are DaemonSets vs StatefulSets vs Jobs?",
         "Write a resource limit and LimitRange from memory."],
    16: ["How does ArgoCD sync a Git repo to Kubernetes?",
         "What is a Helm values file and how do you override defaults?",
         "Draw a full GitOps pipeline from code push to production.",
         "Explain Prometheus metric types.",
         "How do you build a Grafana dashboard from PromQL?"],
    17: ["Explain AlertManager routing and receivers.",
         "What is Grafana Loki and how does it differ from Prometheus?",
         "How does Trivy scan container images for CVEs?",
         "Explain External Secrets Operator with AWS Secrets Manager.",
         "How does CloudWatch Container Insights differ from Prometheus?"],
    18: ["How do you create a ClusterRole and bind it — from memory?",
         "Write a NetworkPolicy from memory — no docs.",
         "Perform an etcd backup command from memory.",
         "Drain a node and schedule a pod with tolerations.",
         "You have 2 hours — how do you prioritize 20 CKA questions?"],
    19: ["Define SLI, SLO, SLA with a real-world example.",
         "What is a service mesh and what problem does mTLS solve?",
         "How does External Secrets Operator sync Vault to K8s?",
         "What is a FinOps tagging strategy?",
         "Write a postmortem template from memory."],
    20: ["Walk through your full GitOps platform end to end.",
         "Explain your self-healing cluster — what triggers remediation?",
         "What makes a great DevOps portfolio README?",
         "Give a STAR answer: Tell me about a time you automated something.",
         "What are your 3 strongest DevOps skills and how do you prove them?"]
}

if __name__ == "__main__":
    weeks = load_roadmap()
    today = date.today()
    delta = (today - START_DATE).days
    week_num = (delta // 7) + 1

    if week_num < 1 or week_num > len(weeks):
        send(f"Weekly review — outside {len(weeks)}-week window (week {week_num}).")
    else:
        week = weeks[week_num - 1]
        theme = week.get("theme", "")
        cert_focus = week.get("cert_focus", "")
        project = week.get("project", "")
        github_goal = week.get("github_goal", "")
        linkedin_goal = week.get("linkedin_goal", "")
        daily_focus = week.get("daily_focus", {})

        q_list = QUESTIONS.get(week_num, QUESTIONS[1])

        # Next week preview
        nxt = weeks[week_num] if week_num < len(weeks) else None
        nxt_text = f"\U0001f4cc <b>Next Week:</b> {nxt['theme']}" if nxt else "\U0001f393 Final week complete!"

        # Build daily focus summary
        focus_str = "\n".join([f"  {d}: {t}" for d, t in daily_focus.items()])

        # Build questions
        q_str = "\n".join([f"  {i+1}. {q}" for i, q in enumerate(q_list)])

        msg = (
            f"\U0001f4dd <b>Weekly Review \u2014 Week {week_num}/{len(weeks)}</b>\n"
            f"\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\n"
            f"\U0001f4da Theme: <b>{theme}</b>\n"
            f"\U0001f3af Cert Focus: {cert_focus}\n"
            f"\U0001f4c1 Project: {project}\n\n"
            f"\u2705 <b>This Week's Daily Topics</b>\n"
            f"{focus_str}\n\n"
            f"\u2705 <b>Completion Checklist</b>\n"
            f"  \u2610 All weekday labs completed\n"
            f"  \u2610 GitHub commits pushed ({github_goal})\n"
            f"  \u2610 Notes written for each topic\n"
            f"  \u2610 LinkedIn: {linkedin_goal}\n\n"
            f"\U0001f9e0 <b>Self-Assessment (answer honestly)</b>\n"
            f"{q_str}\n\n"
            f"\U0001f4ca <b>Rate yourself 1\u201310 for this week: ___</b>\n\n"
            f"\U0001f504 <b>If behind:</b>\n"
            f"  \u2022 Use Saturday for catchup labs\n"
            f"  \u2022 Sunday evening: redo weakest topic\n"
            f"  \u2022 Don't skip ahead \u2014 depth beats speed\n\n"
            f"{nxt_text}\n\n"
            f"\U0001f916 <i>devops-study-bot weekly review</i>"
        )
        send(msg)
        print(f"Weekly review sent for week {week_num}")
