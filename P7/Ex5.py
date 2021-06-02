import http.client
import json
import seq1

dict_genes = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362'
}

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
PARAMETERS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)

try:
    for gene in dict_genes:
        id = dict_genes[gene]
        connection.request("GET", ENDPOINT + id + PARAMETERS)
        response = connection.getresponse()
        if response.status == 200:
            response_dict = json.loads(response.read().decode())
            #print(json.dumps(response_dict, indent=4, sort_keys=True))
            sequence = seq1.Seq(response_dict["seq"])
            s_length = sequence.len()
            a, c, g, t, = sequence.basepercentage()
            most_frequent_base = sequence.frequent_base()
            print("The gene is:", gene)
            print("The length is: ", s_length)
            print("A:", a, "%")
            print("C:", c, "%")
            print("G:", g, "%")
            print("T:", t, "%")
            print("Most frequent base: ", most_frequent_base)

except KeyError:
    print("The gene is not inside our dictionary. Choose one of the following: ", list(dict_genes.keys()))