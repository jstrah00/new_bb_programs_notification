# New Bug Bounty Programs Notification
Notifies on new bug bunty programs (filtered by wildcard type)

# Installation

Add variables specified in `.env.example` to `.env` file.

# Run the project

```bash
 pdm run main.py
```

# Run with docker

Build
```bash
docker build -t new_bb_programs_notification .
```
Run
```bash
docker run --env-file .env new_bb_programs_notification
```

# Run in Kubernetes

Create secrets
```bash
kubectl create secret generic telegram-secrets \
  --from-literal=BOT_TOKEN=abc123 \
  --from-literal=PERSONAL_CHAT_ID=987654321
```

Deploy cronjob
```bash
kubectl apply -f cronjob.yaml
```

