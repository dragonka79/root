import yaml


def import_devices():
    
    with open ("quokka/data/devices.yaml") as devices_file:
        devices = yaml.safe_load(devices_file.read())
        return devices