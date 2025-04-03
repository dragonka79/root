# Generating the subnet address of a IP if the subnet mask is /24

ip = "10.10.10.10"
split_ip = ip.split(".")
print(split_ip)

split_ip[3] = "0"
print(split_ip)

subnet_address = ".".join(split_ip)
print(subnet_address)