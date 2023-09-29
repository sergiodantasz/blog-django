#!/bin/sh

echo "🟡 Executing runserver.sh..."
python manage.py runserver 0.0.0.0:8000
echo "🟢 runserver.sh executed succesfully."
