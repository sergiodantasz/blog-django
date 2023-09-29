#!/bin/sh

echo "🟡 Executing collectstatic.sh..."
python manage.py collectstatic --noinput
echo "🟢 collectstatic.sh executed succesfully."
