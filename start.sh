#!/usr/bin/env bash
set -e

cd backend
pip3 install -r ../requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py runserver 0.0.0.0:$PORT