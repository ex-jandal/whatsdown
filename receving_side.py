from prompt_toolkit.patch_stdout import patch_stdout

def receving_massege(recever_socket, is_true: bool):
    conn, addr = recever_socket.accept()
    while is_true:
        data = conn.recv(1024)
        if data:
            with patch_stdout():
                print(f"<<-| {data.decode("utf-8")}")
        elif not data:
            break

    conn.close()
    recever_socket.close()
    print("Your Partiner are closed.")
