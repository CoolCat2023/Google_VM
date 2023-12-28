#!/usr/bin/env python3

#Writing a simple script to run hello_cloud.py file


#importing socket module

import socket 

#getting the hostname by socket .gethostname() method

hostname=socket.gethostname()

#getting the ip address using socket.gethostname() method

ip_address=socket.gethostbyname(hostname)

#printing the hostname and ip_address 
print("Hello Cloud")
print(f'Hostname: {hostname}')
print(f'IP_address: {ip_address}')

