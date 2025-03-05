import socket

def get_ip() -> str:
    return input("Enter the destination IP: ")

def create_sending_socket(destination_ip: str, PORT: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((destination_ip, PORT))
    return s

def create_receving_socket(PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', PORT))
    s.listen(1)  
    return s

