from quokka.controller.util import import_devices
from quokka import app


@app.route("/devices/")
def devices():
    devices = import_devices()
    return {'devices': devices}