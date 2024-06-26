#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

if [ -z "$AWS_IP_ADDRESS"]
then
    echo "AWS_IP_ADDRESS not defined"
    exit 0
fi

git archive --format tar --output ./project.tar main

echo 'Uploading project...'
rsync ./project.tar root@AWS_IP_ADDRESS:/tmp/project.tar
echo 'Uploading project complete...'

echo 'Build the image...'
ssh -o StrictHostKeyChecking=no root@AWS_IP_ADDRESS << 'ENDSSH'
    mkdir -p /app
    rm -rf /app/* && tar -xf /tmp/project.tar -C /app
    docer compose -f /app/production.yml up --build -d --remove-orphans
ENDSSH
echo 'Build completed...'
