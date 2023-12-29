from colorama import Fore
from time import sleep
import sys

color_white = Fore.WHITE
color_red = Fore.RED
color_green = Fore.GREEN

try:
    while True:

        for remaining in range(10, -1, -1):
            sys.stdout.write("\r")
            if remaining >3:
                sys.stdout.write(
                    f" Refresh:{Fore.GREEN}{remaining:3d}{Fore.WHITE} " \
                    "seconds remaining."
                    )
                sys.stdout.flush()
                sleep(1)
            else:
                sys.stdout.write(
                    f" Refresh:{Fore.RED}{remaining:3d}{Fore.WHITE} " \
                    "seconds remaining."
                    )
                sys.stdout.flush()
                sleep(1)
            
except KeyboardInterrupt:
        print(f"{color_white}\n\nExiting countdown")
        exit()
