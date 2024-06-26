#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

if [ -z "${AWS_IP_ADDRESS:-}" ]; then
    echo "AWS_IP_ADDRESS not defined"
    exit 1
fi

git archive --format tar --output ./project.tar main

echo 'Uploading project...'
rsync -avz -e "ssh -o StrictHostKeyChecking=no -T" ./project.tar marcelogalli@$AWS_IP_ADDRESS:/tmp/project.tar
echo 'Uploading project complete...'

echo 'Build the image...'
ssh -o StrictHostKeyChecking=no marcelogalli@$AWS_IP_ADDRESS << 'ENDSSH'
    mkdir -p /home/marcelogalli/app
    rm -rf /home/marcelogalli/app/* && tar -xf /tmp/project.tar -C /home/marcelogalli/app
    docker compose -f /home/marcelogalli/app/production.yml up --build -d --remove-orphans
ENDSSH
echo 'Build completed...'
