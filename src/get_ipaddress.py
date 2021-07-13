import socket

def get_ipaddress():
    #Getting the hostname
    hostname = socket.gethostname()
    #Getting the IP address
    ip_address = socket.gethostbyname(hostname)
    return ip_address
