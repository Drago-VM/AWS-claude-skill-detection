# Detection Rules

## IAM

- AttachUserPolicy → Privilege Escalation
- CreateAccessKey → Credential Access
- GetUserPolicy → Recon

---

## S3

- GetObject (large volume) → Data Exfil
- PutBucketPolicy → Public Exposure

---

## EC2

- RunInstances → Unexpected compute
- Metadata access → Credential theft

---

## Network

- Unusual outbound traffic
- Suspicious IP

---

## Persistence

- New IAM role trust
- Lambda backdoor