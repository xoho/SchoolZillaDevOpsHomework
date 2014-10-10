#localserver
###############################################################################
# Launches the server
#
# author: eric.hoxworth@gmail.com
###############################################################################


####
# Use for debugging or monitoring - not scalable for production - use application.wsgi + uwsgi + nginx for production
####

from bottle import run
from server import application


run(application, host="0.0.0.0", port=8000, reloader=True)
