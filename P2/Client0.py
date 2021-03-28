import socket
from termcolor import colored

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port =port
    def ping(self): #CHECK IF SERVER WORKS (IF WE RECEIVE RESPONSES FROM IT, IT WORKS)
        print('OK')
    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#if we connect the socket to sth not running:
        try:
            s.connect((self.ip, self.port))
            print('server is up')
        except ConnectionRefusedError:
            print("Could not connect to the server. Is it running? Have you checked the IP and Port?")

    def __str__(self):
        return "Connection to SERVER at " + self.ip + ", PORT: " + str(self.port)
    def talk(self, msg): #receives the message as argument
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data.
        print("To Server:", msg)
        s.send(msg.encode())
        # Receive data
        response = s.recv(2048).decode("utf-8") #this number stablishes the maximum amount of bytes that could go into the socket at max
        # Close the socket
        s.close()
        # Return the response
        return "From server: " + response
    def debug_talk(self, msg):
        response = self.talk(msg)
        color_response = colored(response, 'green')
        print('From Server: ', color_response)