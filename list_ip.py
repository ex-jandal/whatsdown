import psutil
import socket

# Iterate over all network interfaces and their addresses
for interface, addresses in psutil.net_if_addrs().items():
    for address in addresses:
        # Check if the address is an IPv4 address
        if address.family == socket.AF_INET:
            print(f"Interface: {interface}, IP Address: {address.address}")

