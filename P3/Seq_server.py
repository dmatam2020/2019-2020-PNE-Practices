import socket
import Server_utils
import termcolor
from Seq1 import Seq

list_sequences = ["AAAA", "CCCC", "TTTT", "GGGG", "ACTG"]
# gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
IP = "127.0.0.1"
PORT = 8590

SEQ_GET = [
    "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT",
]

FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("Seq server is configured!")
client_address_list = []
count_connections = 0

while True:
    print("Waiting for clients...")
    try:
        (cs, client_ip_port) = ls.accept()
        print("A client has connected to the server!")
        client_address_list.append(client_ip_port)
        count_connections += 1
        print("CONNECTION " + str(count_connections) + ". Client IP, PORT: " + str(client_ip_port))
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        formatted_msg = Server_utils.format_command(msg)
        formatted_msg = formatted_msg.split(" ")
        if len(formatted_msg) == 1:
            command = formatted_msg[0]
        else:
            command = formatted_msg[0]
            argument = formatted_msg[1]
            # print(argument)
        if command == "PING":
            Server_utils.ping()

        elif command == "GET":
            Server_utils.get(list_sequences, cs, argument)

        elif command == "INFO":
            Server_utils.info(cs, argument)

        elif command == "COMP":
            Server_utils.comp(Seq, argument)

        elif command == "REV":
            Server_utils.rev(Seq, argument)

        elif command == "GENE":
            Server_utils.gene(Seq, argument)

        else:
            response = "Not available command"
            termcolor.cprint(response, "red")
            cs.send(response.encode())
        cs.close()