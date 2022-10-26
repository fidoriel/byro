#!/bin/bash

set -e
set -m

cd /byro/src/

echo "makemigration is in progress status"
python3 manage.py makemigrations

echo "Migration is in progress status"
python3 manage.py migrate

echo "collectstatic is in progress"
python3 manage.py collectstatic --no-input

echo "Load Testdata"
python3 manage.py loaddata test_data.json

echo "byro with Django docker is fully configured successfully."

exec "$@"