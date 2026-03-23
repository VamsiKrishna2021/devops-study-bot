#!/usr/bin/env python3
"""Exam Alert — fires once per cert, 7 days before exam date."""
import os, sys, requests

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID   = os.environ["TELEGRAM_CHAT_ID"]
API_URL   = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send(text):
    r = requests.post(API_URL, json={"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"})
    r.raise_for_status()

EXAMS = {
    "aws-saa": {
        "name": "AWS Solutions Architect Associate (SAA-C03)",
        "date": "May 16, 2026",
        "sprint": {
            "Day 1 (Sat)": "IAM deep dive: policies, roles, SCPs, cross-account access",
            "Day 2 (Sun)": "EC2 + VPC: placement groups, ENIs, NACLs vs SGs, NAT GW",
            "Day 3 (Mon)": "S3 + storage: classes, lifecycle, replication, encryption",
            "Day 4 (Tue)": "Databases: RDS Multi-AZ, Aurora, DynamoDB, ElastiCache",
            "Day 5 (Wed)": "HA/DR: ASG, ALB/NLB, Route 53 failover, multi-region",
            "Day 6 (Thu)": "Serverless + containers: Lambda, API GW, ECS, Fargate",
            "Day 7 (Fri)": "Full mock exam (65 Qs, 130 min) → review all wrong answers"
        },
        "top_topics": [
            "IAM policy evaluation logic (explicit deny wins)",
            "S3 storage class transitions and lifecycle",
            "VPC: subnets, route tables, NAT GW vs IGW",
            "RDS Multi-AZ (sync) vs Read Replica (async)",
            "ALB vs NLB: Layer 7 vs Layer 4, sticky sessions",
            "Auto Scaling: target tracking vs step vs simple",
            "Lambda: concurrency, layers, VPC access, cold starts",
            "CloudFront: OAC, cache behaviors, origin failover",
            "SQS vs SNS vs EventBridge decision matrix",
            "DynamoDB: partition key design, GSI vs LSI, DAX",
            "ECS vs EKS vs Fargate decision tree",
            "KMS: CMK types, envelope encryption, key policies",
            "CloudTrail vs Config vs GuardDuty vs Inspector",
            "Route 53 routing policies (weighted, latency, failover)",
            "Well-Architected Framework 6 pillars"
        ],
        "traps": [
            "TRAP: 'cost-effective' usually means S3 IA or Glacier, not Standard",
            "TRAP: Multi-AZ is NOT a read scaling solution — that's Read Replicas",
            "TRAP: NAT Gateway is for outbound only — not inbound from internet",
            "TRAP: Lambda 15-min timeout — long jobs need Step Functions or Fargate",
            "TRAP: 'Minimal operational overhead' = managed service / serverless"
        ]
    },
    "terraform-004": {
        "name": "HashiCorp Terraform Associate 004",
        "date": "May 30, 2026",
        "sprint": {
            "Day 1 (Sat)": "IaC concepts + Terraform workflow: init, plan, apply, destroy",
            "Day 2 (Sun)": "HCL deep dive: variables, outputs, locals, expressions",
            "Day 3 (Mon)": "State management: remote state, locking, import, refresh",
            "Day 4 (Tue)": "Modules: structure, sources, versioning, registry",
            "Day 5 (Wed)": "Terraform Cloud + Sentinel + workspaces + VCS workflows",
            "Day 6 (Thu)": "004-specific: ephemeral resources, provider functions, stacks, test",
            "Day 7 (Fri)": "Full mock exam (57 Qs, 60 min) → review all wrong answers"
        },
        "top_topics": [
            "Terraform workflow: Write → Plan → Apply",
            "State file purpose, remote backends (S3, TF Cloud)",
            "State locking with DynamoDB",
            "terraform import and state mv commands",
            "Variables: types, defaults, validation, sensitive",
            "count vs for_each — when to use each",
            "Module structure: inputs, outputs, versioning",
            "Module sources: local, registry, GitHub, S3",
            "Terraform Cloud: VCS-driven vs CLI-driven runs",
            "Sentinel: policy-as-code, enforcement levels",
            "Workspaces: CLI workspaces vs TF Cloud workspaces",
            "Provider configuration: version constraints, alias",
            "NEW in 004: Ephemeral resources",
            "NEW in 004: Provider-defined functions",
            "NEW in 004: Terraform stacks and deployments"
        ],
        "traps": [
            "TRAP: terraform apply -auto-approve skips plan confirmation, not plan itself",
            "TRAP: Workspaces in CLI ≠ Workspaces in Terraform Cloud",
            "TRAP: terraform fmt only fixes style — validate checks config syntax",
            "TRAP: Module versions only work with registry sources, not GitHub",
            "TRAP: Sensitive variables still appear in state file — state must be secured"
        ]
    },
    "cka": {
        "name": "Certified Kubernetes Administrator (CKA)",
        "date": "August 1, 2026",
        "sprint": {
            "Day 1 (Sat)": "Cluster setup: kubeadm init, join, static pods, certificates",
            "Day 2 (Sun)": "Workloads: Deployments, rollouts, Jobs, CronJobs, DaemonSets",
            "Day 3 (Mon)": "Networking: Services, Ingress, NetworkPolicy, DNS, CNI",
            "Day 4 (Tue)": "Storage: PV, PVC, StorageClass, volume expansion",
            "Day 5 (Wed)": "Security: RBAC, ServiceAccounts, SecurityContext, etcd backup",
            "Day 6 (Thu)": "Troubleshooting: node NotReady, pod failures, networking debug",
            "Day 7 (Fri)": "killer.sh full simulation (2 hours) → review all missed"
        },
        "top_topics": [
            "kubeadm cluster bootstrap and upgrade",
            "etcd backup (snapshot save) and restore",
            "RBAC: Role, ClusterRole, RoleBinding, ClusterRoleBinding",
            "NetworkPolicy: ingress/egress rules, namespace selectors",
            "PV/PVC lifecycle, StorageClass, access modes",
            "Deployment rollout, rollback, scale commands",
            "Service types: ClusterIP, NodePort, LoadBalancer",
            "Ingress controller + Ingress resource configuration",
            "ConfigMap and Secret: create, mount, inject as env",
            "Node drain, cordon, uncordon process",
            "Static pods: create by placing YAML in manifest path",
            "kubectl imperative: create, expose, run, set image",
            "Logging: kubectl logs, describe, events, journalctl",
            "Resource requests and limits, LimitRange, ResourceQuota",
            "Scheduling: nodeSelector, affinity, taints, tolerations"
        ],
        "traps": [
            "TRAP: Use kubectl docs in the exam — bookmark key pages beforehand",
            "TRAP: Always set the right context (kubectl config use-context) per question",
            "TRAP: etcd restore requires stopping API server first",
            "TRAP: NetworkPolicy with empty podSelector {} selects ALL pods in namespace",
            "TRAP: Read the question weight — do 8% questions last, 13% first"
        ],
        "extra": (
            "\n⚡ <b>killer.sh Strategy</b>\n"
            "  • You get 2 free sessions with CKA registration\n"
            "  • Session 1: Take untimed, learn the environment\n"
            "  • Session 2: Take timed (2 hrs), simulate real exam\n"
            "  • killer.sh is harder than real exam — 60%+ here = pass\n\n"
            "📖 <b>Open-Book Tips</b>\n"
            "  • Bookmark: kubernetes.io/docs, kubectl cheat sheet\n"
            "  • Practice finding docs pages in < 30 seconds\n"
            "  • Use kubectl explain <resource> instead of googling"
        )
    }
}

if __name__ == "__main__":
    exam_key = sys.argv[1] if len(sys.argv) > 1 else "aws-saa"
    exam = EXAMS.get(exam_key)

    if not exam:
        print(f"Unknown exam: {exam_key}")
        sys.exit(1)

    sprint_str = "\n".join([f"  <b>{day}:</b> {task}" for day, task in exam["sprint"].items()])
    topics_str = "\n".join([f"  {i+1}. {t}" for i, t in enumerate(exam["top_topics"])])
    traps_str  = "\n".join([f"  ⚠️ {t}" for t in exam["traps"]])
    extra_str  = exam.get("extra", "")

    msg1 = (
        f"🚨 <b>EXAM ALERT — {exam['name']}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📅 Exam Date: <b>{exam['date']}</b>\n"
        f"⏰ 7 days to go — sprint starts NOW\n\n"
        f"📋 <b>7-Day Sprint Plan</b>\n"
        f"{sprint_str}"
    )

    msg2 = (
        f"📚 <b>Top 15 Exam Topics — {exam['name']}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{topics_str}"
    )

    msg3 = (
        f"⚠️ <b>Common Exam Traps</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{traps_str}\n"
        f"{extra_str}\n\n"
        f"✅ <b>Exam-Day Checklist</b>\n"
        f"  ☐ Good night's sleep (7+ hours)\n"
        f"  ☐ ID and exam confirmation ready\n"
        f"  ☐ Quiet room, stable internet\n"
        f"  ☐ Water and snack nearby\n"
        f"  ☐ Read every question twice before answering\n"
        f"  ☐ Flag hard questions — come back later\n"
        f"  ☐ Trust your preparation. You've done the work.\n\n"
        f"🤖 <i>devops-study-bot exam alert — YOU GOT THIS.</i>"
    )

    send(msg1)
    send(msg2)
    send(msg3)
    print(f"Exam alert sent for {exam_key}")
