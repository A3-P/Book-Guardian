web: python manage.py collectstatic --noinput && python manage.py migrate && gunicorn --workers=3 --timeout=120 setup.wsgi:application
