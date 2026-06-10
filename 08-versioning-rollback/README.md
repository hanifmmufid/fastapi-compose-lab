# Docker Image Versioning and Rollback

## Problem

Using only `latest` tag is risky because it is unclear which version is running and rollback becomes difficult.

## Solution

Each image is tagged with:

- latest
- commit SHA short

Example:

```text
ghcr.io/hanifmmufid/fastapi-compose-lab:latest
ghcr.io/hanifmmufid/fastapi-compose-lab:abc1234
Deploy
cd /home/ubuntu/deploy/fastapi-compose-lab
./deploy.sh
Rollback
cd /home/ubuntu/deploy/fastapi-compose-lab
./rollback.sh abc1234
Check App
curl http://localhost:8000
curl http://localhost:8000/health
curl http://localhost:8000/db-check
Important Lesson

Production deployment should be traceable to a specific image tag or commit SHA.
