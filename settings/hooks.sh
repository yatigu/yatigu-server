#!/bin/sh
echo "push"
git checkout -t origin/deploy
git pull origin deploy
fuser -k -n tcp 8000
export MODE=RUN
python3 manage.py runserver
