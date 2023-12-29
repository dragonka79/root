from colorama import Fore
from time import sleep
import sys

hosts = {
    "1": "zolcs",
    "2": "zsu"
}
for host in hosts:
    if hosts[host] == "zolcs":
        color = Fore.RED
    else:
        color = Fore.GREEN
    print(color + hosts[host] + Fore.WHITE) # print hosts + switching back to 
                                            # font color white
    
try:
    while True:

        for remaining in range(10, -1, -1):
            sys.stdout.write("\r")
            sys.stdout.write(f"  Refresh: {remaining:3d} seconds remaining.")
            sys.stdout.flush()
            sleep(1)
except KeyboardInterrupt:
        print("\n\nExiting countdown")
        exit()


