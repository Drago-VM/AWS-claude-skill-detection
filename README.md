<!-- 🔥 Banner -->


<h1 align="center">🚨 AWS Security Detection Skill</h1>
<p align="center">
<b>Claude-Powered Cloud Security Detection System</b><br>

> LLM-assisted detection engineering for AWS environments. Built for Detection & Response engineers who think in detections, not just alerts.

---

## What's in this Skill

This is a Claude **skill** — a structured knowledge pack that turns Claude into a specialized AWS security detection engineer. It includes:

```
AWS-claude-skill-detection
│
├── SKILL.md
├── DETECTIONS.md
├── PLAYBOOKS.md
├── PROMPTS.md
├── REFERENCE.md
│
├── modules/
│   ├── iam.md
│   ├── s3.md
│   ├── ec2.md
│   ├── network.md
│   └── persistence.md
│
├── scenarios/
│   ├── root_login.md
│   ├── iam_recon.md
│   ├── s3_access.md
│   └── cloudtrail_digest.md
│
├── data/
│   ├── sample_events.json
│
├── scripts/
│   └── run_analysis.py
│
└── README.md
```
---

## Detection Coverage

All detections are mapped to **MITRE ATT&CK Cloud Matrix**:

| Domain | Coverage |
|--------|----------|
| **Initial Access** | Credential stuffing, console login anomalies |
| **Credential Access** | Secrets Manager exfil, IMDS theft, key enumeration |
| **Privilege Escalation** | IAM policy manipulation, role trust modification |
| **Defense Evasion** | CloudTrail disabled, GuardDuty muted, SCP removed |
| **Persistence** | Lambda backdoors, OIDC hijack, new IAM users |
| **Exfiltration** | S3 mass download, replication to external account |
| **Impact** | Bucket deletion, ransomware via encryption change |
| **Lateral Movement** | Cross-account AssumeRole, SSH/RDP scanning |

---
