import socket

IP = "192.168.0.241"
PORT = 139

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((IP, PORT))

s.send(str.encode("HELLO FROM THE CLIENT!!!"))

#msg = s.recv(2048)
#print("MESSAGE FROM THE SERVER:\n")
#print(msg.decode('ISO-8859-1'))

s.close()