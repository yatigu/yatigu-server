#!/bin/sh
echo "push"
git checkout -t origin/master
git pull origin master
fuser -k -n tcp 8000
python3 manage.py runserver
