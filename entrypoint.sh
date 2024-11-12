#!/bin/sh

# Wait for the database to be available
echo "Waiting for database..."
until nc -z -v -w30 db 5432; do
  echo "Waiting for db to be ready..."
  sleep 2
done

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Start the Django development server
exec "$@"
