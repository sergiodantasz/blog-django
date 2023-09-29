#!/bin/sh

echo "🟡 Executing makemigrations.sh..."
python manage.py makemigrations --noinput
echo "🟢 makemigrations.sh executed succesfully."
