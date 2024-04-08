import logging
import os
from chalice import Chalice


APP_NAME = "template"

app = Chalice(app_name=APP_NAME)

environment = os.environ.get("ENVIRONMENT")

if environment != "prod":
    app.log.setLevel(logging.DEBUG)
    app.debug = True


@app.route('/', methods=['GET'], content_types=['application/json'])
def index():
    request = app.current_request
    print(request)
    return {'hello': 'world'}
