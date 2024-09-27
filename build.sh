#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt
python manage.py collectstatic --no-input

python manage.py makemigrations inventories
python manage.py makemigrations suppliers
python manage.py makemigrations sales
python manage.py makemigrations storage

# Apply any outstanding database migrations
python manage.py migrate