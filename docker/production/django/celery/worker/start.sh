#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

exec celery -A app.celery_app worker -l INFO