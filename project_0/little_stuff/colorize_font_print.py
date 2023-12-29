from colorama import Fore

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
 