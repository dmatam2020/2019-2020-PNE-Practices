import socket
import colorama
import termcolor

# Configure the Server's IP and PORT
PORT = 52123
IP = "127.0.0.1" #(substitute by the local one) #PORT always a int; IP always string
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        colorama.init(strip='False')
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(msg))

        # Send the messag
        message = "Helloo from the teacher's server"
        send_bytes = str.encode(message)
        # We must write bytes, not a string
        clientsocket.send(message.encode())
        clientsocket.close()

except socket.error:
    print("roblems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()