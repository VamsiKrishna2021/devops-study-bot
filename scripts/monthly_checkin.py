#!/usr/bin/env python3
"""Monthly Check-in — fires 23rd of each month 8 PM CDT."""
import os, requests
from datetime import date

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID   = os.environ["TELEGRAM_CHAT_ID"]
API_URL   = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send(text):
    r = requests.post(API_URL, json={"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"})
    r.raise_for_status()

MONTHS = {
    3: {
        "month_name": "March",
        "week_range": "Week 1",
        "skills": [
            "Linux filesystem and permissions",
            "Bash scripting (loops, conditionals, functions)",
            "Systemd services and cron jobs",
            "Networking CLI (ss, curl, dig, nmap)",
            "Git branching, PRs, rebase"
        ],
        "projects": ["devops-study-bot (this repo!)"],
        "cert_status": "AWS SAA study begins next month",
        "linkedin": "Update headline to 'Aspiring DevOps Engineer | AWS | Terraform | Kubernetes'"
    },
    4: {
        "month_name": "April",
        "week_range": "Weeks 2–5",
        "skills": [
            "Docker: images, multi-stage builds, networking, volumes, Compose",
            "AWS IAM: users, roles, policies, STS, MFA",
            "AWS EC2: ASG, ALB/NLB, Lambda, Fargate",
            "AWS S3: storage classes, lifecycle, presigned URLs",
            "AWS RDS: Multi-AZ, read replicas, DynamoDB GSI"
        ],
        "projects": [
            "docker-compose-stack (Flask + Redis + Postgres)",
            "lambda-s3-dynamo (event-driven pipeline)",
            "s3-presigned-url (Python generator)"
        ],
        "cert_status": "AWS SAA — actively studying (Weeks 3–6)",
        "linkedin": "Post: 'Built my first Docker multi-stage pipeline' with screenshot"
    },
    5: {
        "month_name": "May",
        "week_range": "Weeks 6–9",
        "skills": [
            "AWS VPC: 3-tier architecture, peering, Transit GW",
            "Route 53: failover, weighted, latency routing",
            "CloudFront + WAF + Shield",
            "Terraform: HCL, state, modules, workspaces",
            "Terraform Cloud, Sentinel, 004 new features"
        ],
        "projects": [
            "vpc-3tier-lab (full networking stack)",
            "tf-vpc-module (reusable Terraform module)",
            "tf-sentinel-policy (policy-as-code)"
        ],
        "cert_status": "AWS SAA exam ~May 16 | Terraform 004 exam ~May 30",
        "linkedin": "Post: 'Passed AWS SAA!' (if done) + share VPC architecture diagram"
    },
    6: {
        "month_name": "June",
        "week_range": "Weeks 10–14",
        "skills": [
            "Kubernetes: pods, deployments, services, StatefulSets",
            "K8s networking: CNI, NetworkPolicy, Ingress, CoreDNS",
            "K8s security: RBAC, ServiceAccounts, Pod Security Standards",
            "K8s storage: PV, PVC, StorageClass, dynamic provisioning",
            "K8s ops: scheduling, HPA, cluster upgrades, troubleshooting"
        ],
        "projects": [
            "k8s-cluster-setup (kubeadm from scratch)",
            "k8s-network-policy (namespace isolation)",
            "k8s-ingress-tls (TLS termination + path routing)",
            "etcd-backup-restore (CKA critical skill)"
        ],
        "cert_status": "Terraform 004 passed (if done) | CKA study in full swing",
        "linkedin": "Post: 'Built a Kubernetes cluster from scratch with kubeadm' + diagram"
    },
    7: {
        "month_name": "July",
        "week_range": "Weeks 15–17",
        "skills": [
            "CI/CD: GitHub Actions, OIDC, matrix builds",
            "GitOps: ArgoCD, Helm charts, full pipeline",
            "Monitoring: Prometheus, Grafana, AlertManager",
            "Observability: OpenTelemetry, Jaeger, CloudWatch",
            "CKA exam prep: killer.sh, kubectl speed drills"
        ],
        "projects": [
            "full-gitops-pipeline (GitHub → ECR → ArgoCD → K8s)",
            "prometheus-grafana-stack (5-panel dashboard)",
            "alertmanager-telegram (alert integration)"
        ],
        "cert_status": "CKA exam ~August 1 | Final sprint week 17",
        "linkedin": "Post: 'Built a full GitOps pipeline with ArgoCD' + architecture diagram"
    },
    8: {
        "month_name": "August",
        "week_range": "Weeks 18–20",
        "skills": [
            "Terragrunt: DRY multi-environment configs",
            "Ansible: playbooks, roles, vault",
            "Packer: golden AMI baking",
            "SRE: SLOs, error budgets, service mesh, secrets management",
            "Capstone: full platform end-to-end"
        ],
        "projects": [
            "capstone-gitops-platform (Terraform + ArgoCD + monitoring)",
            "capstone-self-healing (HPA + PDB + auto-remediation)",
            "Portfolio polish: architecture diagrams on all repos"
        ],
        "cert_status": "CKA passed (if done) | All 3 certs complete",
        "linkedin": "Full portfolio update: headline, summary, 3 featured projects, resume refresh"
    }
}

if __name__ == "__main__":
    today = date.today()
    month_num = today.month
    data = MONTHS.get(month_num)

    if not data:
        send(f"📅 Monthly check-in — no data for month {month_num}. Program runs March–August.")
    else:
        skills_str   = "\n".join([f"  {'✅' if False else '☐'} {s}" for s in data["skills"]])
        projects_str = "\n".join([f"  📁 {p}" for p in data["projects"]])

        msg = (
            f"📊 <b>Monthly Check-in — {data['month_name']} 2026</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"📅 Covering: <b>{data['week_range']}</b>\n\n"
            f"🛠 <b>Skills You Should Have By Now</b>\n"
            f"{skills_str}\n\n"
            f"📁 <b>GitHub Projects Expected</b>\n"
            f"{projects_str}\n\n"
            f"🎓 <b>Certification Status</b>\n"
            f"  {data['cert_status']}\n\n"
            f"💼 <b>LinkedIn Action Item</b>\n"
            f"  {data['linkedin']}\n\n"
            f"📈 <b>Am I On Track?</b>\n"
            f"  ✅ All skills above feel solid → ON TRACK\n"
            f"  ⚠️ 1–2 gaps → Use this weekend to catch up\n"
            f"  🔴 3+ gaps → Pause and revisit before moving forward\n\n"
            f"🤖 <i>devops-study-bot monthly check-in | {today.strftime('%Y-%m-%d')}</i>"
        )
        send(msg)
        print(f"Monthly check-in sent for {data['month_name']}")
