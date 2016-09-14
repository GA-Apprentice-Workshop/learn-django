serve:
    python manage.py runserver

test:
    python manage.py test learn_django.apps.${TEST_PATH}

routes:
    python manage.py show_urls