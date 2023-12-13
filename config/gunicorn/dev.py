"""Gunicorn *development* config file"""

# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "personal_portfolio.wsgi:application"
# The granularity of Error log outputs
loglevel = "debug"
# The number of worker processes for handling requests
workers = 2
# The socket to bind
bind = '10.0.0.152:8000'
# Restart workers when code changes (development only!)
reload = True
# Redirect stdout/stderr to log file
capture_output = True
# Daemonize the Gunicorn process (detach & enter background)
daemon = True
