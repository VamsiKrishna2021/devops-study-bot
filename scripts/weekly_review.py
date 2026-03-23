#!/usr/bin/env python3
"""Weekly Review — fires Sunday 7 PM CDT via GitHub Actions."""
import json, os, requests
from datetime import date

BOT_TOKEN  = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID    = os.environ["TELEGRAM_CHAT_ID"]
API_URL    = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
START_DATE = date(2026, 3, 23)

def send(text):
    r = requests.post(API_URL, json={"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"})
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
    2:  ["What happens in each layer of a Docker image build?",
         "Why use multi-stage builds? What problem do they solve?",
         "Explain Docker bridge networking — how do two containers talk?",
         "What is the difference between a volume and a bind mount?",
         "Write a docker-compose.yml with 3 services from memory."],
    3:  ["What is the difference between an IAM Role and an IAM User?",
         "Explain the policy evaluation logic — explicit deny vs allow.",
         "What is STS AssumeRole and when would you use it?",
         "How do you list all EC2 instances across all regions with CLI?",
         "What does CloudTrail track that CloudWatch does not?"],
    4:  ["What is the difference between a launch template and launch config?",
         "How does an ALB route traffic differently than an NLB?",
         "Explain Lambda cold starts — what causes them and how to reduce?",
         "What is a target group health check and why does it matter?",
         "When would you choose Fargate over ECS on EC2?"],
    5:  ["Name all S3 storage classes and when to use each.",
         "How does S3 versioning interact with lifecycle rules?",
         "Explain RDS Multi-AZ vs Read Replica — what fails over?",
         "What is a DynamoDB GSI and how does it differ from an LSI?",
         "When would you use EFS instead of EBS?"],
    6:  ["Draw a 3-tier VPC from memory — subnets, route tables, gateways.",
         "What is the difference between a NACL and a Security Group?",
         "Explain Route 53 failover routing with health checks.",
         "What is CloudFront OAC and why replace OAI?",
         "How does AWS WAF rate limiting work at the ALB level?"],
    7:  ["Explain the AWS Shared Responsibility Model with 3 examples.",
         "Design a highly available web app — draw the architecture.",
         "What are the 5 pillars of the Well-Architected Framework?",
         "When do you use SQS vs SNS vs EventBridge?",
         "Explain S3 eventual consistency vs strong consistency."],
    8:  ["What is Terraform state and why is remote state important?",
         "Explain the difference between count and for_each.",
         "How do you structure a reusable Terraform module?",
         "What does terraform plan show that apply doesn't?",
         "What is a data source in Terraform and when do you use one?"],
    9:  ["Explain Terraform workspaces — when to use vs directory structure.",
         "What is Sentinel and how does it enforce policy-as-code?",
         "What are ephemeral resources in Terraform 004?",
         "How does VCS-driven workflow differ from CLI-driven in TF Cloud?",
         "Write a terraform test block for a module from memory."],
    10: ["Explain the Terraform core workflow: Write → Plan → Apply.",
         "What is the purpose of terraform.lock.hcl?",
         "How do you handle secrets in Terraform without hardcoding?",
         "What are the 4 new features in Terraform 004 vs 003?",
         "Explain provider versioning and constraint syntax."],
    11: ["Name all control plane components and what each does.",
         "What is the difference between a Deployment and a StatefulSet?",
         "Explain ClusterIP vs NodePort vs LoadBalancer services.",
         "How do you inject a Secret as an environment variable in a Pod?",
         "Write a kubectl command to create a deployment with dry-run."],
    12: ["What does a CNI plugin do in Kubernetes?",
         "Write a NetworkPolicy that allows only frontend to reach backend.",
         "Explain Ingress TLS termination — where does HTTPS end?",
         "What is the relationship between PV, PVC, and StorageClass?",
         "How does CoreDNS resolve service names across namespaces?"],
    13: ["Explain Role vs ClusterRole — when do you need each?",
         "What is a ServiceAccount token and how is it projected into Pods?",
         "What are Pod Security Standards (Restricted vs Baseline)?",
         "How does OPA Gatekeeper enforce admission policies?",
         "Walk through an etcd backup and restore from memory."],
    14: ["Explain nodeAffinity vs podAffinity vs taints/tolerations.",
         "How does HPA decide when to scale and how fast?",
         "Walk through a kubeadm cluster upgrade step by step.",
         "A pod is in CrashLoopBackOff — what are your first 5 commands?",
         "What is the difference between kubectl logs and stern?"],
    15: ["Explain GitHub Actions: triggers, jobs, and steps relationship.",
         "What is OIDC and why is it better than static AWS credentials?",
         "How does ArgoCD sync a Git repo to a Kubernetes cluster?",
         "What is a Helm values file and how do you override defaults?",
         "Draw a full GitOps pipeline from code push to production."],
    16: ["What are the 4 Prometheus metric types?",
         "How do you build a Grafana dashboard panel from a PromQL query?",
         "Explain AlertManager routing — how do alerts reach Telegram?",
         "What is distributed tracing and what problem does it solve?",
         "How does CloudWatch Container Insights differ from Prometheus?"],
    17: ["How do you create a ClusterRole and bind it to a user — from memory?",
         "Write a NetworkPolicy from memory — no docs.",
         "Perform an etcd backup command from memory.",
         "Drain a node and schedule a pod with tolerations — from memory.",
         "You have 2 hours — how do you prioritize 20 CKA questions?"],
    18: ["What does Terragrunt add on top of Terraform?",
         "Explain Ansible idempotency — how is it different from scripts?",
         "What is a Packer AMI and why bake images instead of bootstrap?",
         "When would you choose AWS CDK over Terraform?",
         "What does Checkov scan for that terraform validate does not?"],
    19: ["Define SLI, SLO, SLA with a real-world example.",
         "What is a service mesh and what problem does mTLS solve?",
         "How does External Secrets Operator sync Vault to K8s Secrets?",
         "What is a FinOps tagging strategy and why does it matter?",
         "Write a postmortem template from memory."],
    20: ["Walk through your full GitOps platform end to end.",
         "Explain your self-healing cluster — what triggers remediation?",
         "What makes a great DevOps portfolio README?",
         "Give a STAR answer for: Tell me about a time you automated something.",
         "What are your 3 strongest DevOps skills and how do you prove them?"]
}

if __name__ == "__main__":
    roadmap = load_roadmap()
    today   = date.today()
    delta   = (today - START_DATE).days
    week_num = (delta // 7) + 1
    weeks    = roadmap["weeks"]

    if week_num < 1 or week_num > len(weeks):
        send(f"📅 Weekly review — outside 20-week window (week {week_num}).")
    else:
        week = weeks[week_num - 1]
        q_list = QUESTIONS.get(week_num, QUESTIONS[1])

        # Next week preview
        nxt = weeks[week_num] if week_num < len(weeks) else None
        nxt_text = f"📌 <b>Next Week Preview:</b> {nxt['theme']}" if nxt else "🎓 Final week complete!"

        # Build questions string
        q_str = "\n".join([f"  {i+1}. {q}" for i, q in enumerate(q_list)])

        msg = (
            f"📝 <b>Weekly Review — Week {week_num}/20</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"📚 Theme: <b>{week['theme']}</b>\n"
            f"🎯 Cert Focus: {week['cert_focus']}\n\n"
            f"✅ <b>Completion Checklist</b>\n"
            f"  ☐ All 5 daily labs completed\n"
            f"  ☐ All 5 GitHub commits pushed\n"
            f"  ☐ Notes written for each topic\n"
            f"  ☐ No skipped days\n\n"
            f"🧠 <b>Self-Assessment (answer honestly)</b>\n"
            f"{q_str}\n\n"
            f"📊 <b>Rate yourself 1–10 for this week: ___</b>\n\n"
            f"🔄 <b>If behind:</b>\n"
            f"  • Use Saturday for catchup labs\n"
            f"  • Sunday evening: redo weakest topic\n"
            f"  • Don't skip ahead — depth beats speed\n\n"
            f"{nxt_text}\n\n"
            f"🤖 <i>devops-study-bot weekly review</i>"
        )
        send(msg)
        print(f"Weekly review sent for week {week_num}")
