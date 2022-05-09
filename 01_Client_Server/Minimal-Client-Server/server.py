import socket

server_socket = socket.socket(socket.AF_INET, 
                              socket.SOCK_STREAM)


ip = "127.0.0.1"
server_addr = (ip, 1337)
server_socket.bind(server_addr)

valid_max_client_number = 1  # for > 1  see multithreading
server_socket.listen(valid_max_client_number)

while True:
    (client_socket, addr) = server_socket.accept()
    # multithreading shall beginn here
    # client_thread = client_thread(client_socket)
    # client_thread.run()

    message = client_socket.recv(2048)
    message_decoded = str(message, "utf8")
    print(message_decoded)
