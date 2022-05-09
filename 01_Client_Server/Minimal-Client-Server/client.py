import socket

client_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)  # SOCK_DGRAM: UDP Socket / SOCK_Stream: TCP Socket

server_addr = ("127.0.0.1", 1337)
client_socket.connect(server_addr)

message = bytes("Hi", "utf8")
client_socket.send(message)
