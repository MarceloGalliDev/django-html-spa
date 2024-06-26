#!/bin/bash

set -o errexit
set -o nounset

worker_ready(){
    celery -A app.celery_app inspect ping
}

until worker_ready; do

>&2 echo "Celery workers not available!"

sleep 1

done

>&2 echo "Celery workers are available and ready!"

exec celery \
    -A app.celery_app \
    -b "${CELERY_BROKER_URL}" \
    flower \
    --basic-auth="${CELERY_FLOWER_USER}:${CELERY_FLOWER_PASSWORD}"

