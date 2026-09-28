#!/usr/bin/env bash
# exit on error
set -o errexit

# Install python dependencies
pip install -r requirements.txt

# Collect static files (CSS, Bootstrap assets)
python Django/django_project/manage.py collectstatic --no-input

# Run database migrations
python Django/django_project/manage.py migrate
