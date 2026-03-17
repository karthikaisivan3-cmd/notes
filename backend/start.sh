#!/usr/bin/env bash
# exit on error
set -o errexit

gunicorn notesharing.wsgi:application --bind 0.0.0.0:$PORT
