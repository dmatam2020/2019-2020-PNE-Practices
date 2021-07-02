import http.client
import json


PORT = 8080
SERVER = "127.0.0.1"
connect = http.client.HTTPConnection(SERVER, PORT)


def client(ARGUMENTS, PATH_NAME):
        connect.request("GET", PATH_NAME + ARGUMENTS)
        # Read the response message from the server
        r1 = connect.getresponse()

        # Print the status line
        print(f"Response received!: {r1.status} {r1.reason}\n")

        # Read the response's body
        data1 = r1.read().decode("utf-8")
        # Print the received data
        data = json.loads(data1)
        return data


try:
    ARGUMENTS = "?limit=10&json=1"
    PATH_NAME = "/listSpecies"
    data = client(ARGUMENTS, PATH_NAME)
    list_names = " "
    for name in data["species_list"]:
        list_names = list_names + name + ", "
    print("The total number of species in the ensemble is: ", data["length"])
    print("The limit you have selected is: ", data["input_number"])
    print("The names of the species are", list_names)

except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

try:
    ARGUMENTS = "?specie=human&json=1"
    PATH_NAME = "/karyotype"
    data = client(ARGUMENTS, PATH_NAME)
    print("The names of the chromosomes are: ", data["list_karyotype"])

except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

try:
    ARGUMENTS = "?specie=human&chromo=18&json=1"
    PATH_NAME = "/chromosomeLength"
    data = client(ARGUMENTS, PATH_NAME)
    print("The length of the chromosome is: ", data["length_chromosome"])

except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

try:
    ARGUMENTS = "?gene=ADA&json=1"
    PATH_NAME = "/geneSeq"
    data = client(ARGUMENTS, PATH_NAME)
    print("The sequence of this gene is: ", data["seq"])

except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

try:
    ARGUMENTS = "?gene_info=ADA&json=1"
    PATH_NAME = "/geneInfo"
    data = client(ARGUMENTS, PATH_NAME)
    print("The start of this gene is:", data["start"])
    print("The end of this gene is:", data["end"])
    print("The length of this gene is:", data["length_sequence"])
    print("The ID of this gene is:", data["ID"])
    print("This gene is found in:", data["chromosome_name"])

except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

try:
    ARGUMENTS = "?gene_calculations=ADA&json=1"
    PATH_NAME = "/geneCalc"
    data = client(ARGUMENTS, PATH_NAME)
    print("The length of this gene is: ", data["total_length"])
    print("The % of base A is: ", data["percentage_a"])
    print("The % of base C is: ", data["percentage_c"])
    print("The % of base G is: ", data["percentage_g"])
    print("The % of base T is: ", data["percentage_t"])


except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()