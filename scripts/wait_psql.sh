#!/bin/sh

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "🟡 Waiting for Postgres database startup ($POSTGRES_HOST $POSTGRES_PORT)..."
  sleep 2
done
echo "🟢 Postgres database started succesfully ($POSTGRES_HOST $POSTGRES_PORT)."
