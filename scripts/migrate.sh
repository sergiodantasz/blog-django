#!/bin/sh

echo "🟡 Executing migrate.sh..."
python manage.py migrate --noinput
echo "🟢 migrate.sh executed succesfully."
