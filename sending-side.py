import establishing_connection

PORT = 5000
destination_ip = establishing_connection.get_ip()

sender_socket = establishing_connection.create_sending_socket(destination_ip, PORT)
print(f"Connected to {destination_ip}:{PORT}")

while True:
    message = input("-> ")
    if not message:  
        break
    sender_socket.send(message.encode('utf-8'))

sender_socket.close()
print("Client closed.")
