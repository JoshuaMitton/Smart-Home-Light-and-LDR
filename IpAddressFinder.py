#!/usr/bin/python
import socket
#import ping

ip_address_up = []

addr_range = "192.168.0.%d"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.settimeout(2.0)

for i in range(1, 254):
    try:
        ip = addr_range % i
        socket.gethostbyaddr(ip)
        ip_address_up.append(ip)
    except socket.herror as ex:
        pass

print ip_address_up
