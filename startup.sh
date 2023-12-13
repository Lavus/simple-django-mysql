#!/bin/bash
python manage.py collectstatic && sed -i 's/bind = .*/bind = '"'`hostname -I | awk '{print $1}'`:8000'"'/' config/gunicorn/dev.py && gunicorn -c config/gunicorn/dev.py