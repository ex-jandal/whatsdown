import establishing_connection

PORT = 5000
recever_socket = establishing_connection.create_receving_socket(PORT)
print(f"Server listening on port {PORT}...")

conn, addr = recever_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print("-|", data.decode('utf-8'))

conn.close()
recever_socket.close()
print("Server closed.")

