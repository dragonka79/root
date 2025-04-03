from tabulate import tabulate
from util.create_utils import create_devices

# --- Main program --------------------------------------------
if __name__ == '__main__':

    devices = create_devices(num_subnets=5, num_devices=3)
    #devices = create_devices(num_subnets=5, num_devices=3)
    print("\n", tabulate(devices, headers="keys"))