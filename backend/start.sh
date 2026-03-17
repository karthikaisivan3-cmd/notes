#!/usr/bin/env bash
# exit on error
set -o errexit

python keep_alive.py &
gunicorn notesharing.wsgi:application --bind 0.0.0.0:$PORT
