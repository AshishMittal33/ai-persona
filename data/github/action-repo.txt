# Action Repo

This repository is used only to generate GitHub events for testing webhooks.

## Purpose
- Create PUSH events
- Create PULL REQUEST events
- Create MERGE events

These events are sent to the backend service in **webhook-repo** using GitHub Webhooks.

## How it works
1. Make a commit → PUSH event
2. Create a pull request → PR event
3. Merge the pull request → MERGE event

## Webhook
Webhook is configured to send events to:

https://<ngrok-url>/webhook

(Content type: application/json)

## Notes
- No backend code here
- This is a dummy repo for event generation only

## Demo

https://youtu.be/f2GTOpM8ueA
