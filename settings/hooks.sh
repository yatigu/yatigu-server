#!/bin/sh
echo "push"
git checkout -t origin/tickets
git pull origin tickets
fuser -k -n tcp 8000
python3 manage.py runserver
