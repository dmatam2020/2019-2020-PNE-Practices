import http.server
import http.client
import socketserver
from urllib.parse import urlparse, parse_qs
from pathlib import Path
import json
import jinja2


PORT = 8080
SERVER = "rest.ensembl.org"
PARAMS = "?content-type=application/json"

DICT_GENES= {"FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839", "FXN": "ENSG00000165060",
"RNU6_269P": "ENSG00000212379", "MIR633": "ENSG00000207552", "TTTY4C":"ENSG00000228296",
"RBMY2YP":"ENSG00000227633", "FGFR3": "ENSG00000068078", "KDR": "ENSMUSG000000629602", "ANK2":"ENSG00000145362"}

socketserver.TCPServer.allow_reuse_address = True

def read_template_html_file(filename):
    content = jinja2.Template(Path(filename).read_text())
    return content


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters: ", arguments)

        context = {}
        content_type = "text/html"

        if path_name == "/":
            contents = read_template_html_file("index.html").render()

        elif path_name == "/listSpecies":
            chk = "chk" in arguments
            try:
                ENDPOINT = "info/species"
                connection = http.client.HTTPConnection(SERVER)
                connection.request("GET", ENDPOINT + PARAMS)
                response = connection.getresponse().read().decode()
                limit = arguments["limit"][0]
                dictionary_response = json.loads(response)
                dictionary_values = dictionary_response.values()
                list_species =[]
                for dictionary in dictionary_values:
                    for element in dictionary:
                        species = element["common_name"]
                        list_species.append(species)
                context["input_number"] = limit
                list_final_species = []

                try:
                    integer_limit = int(limit)
                except ValueError:
                    contents = read_template_html_file("error.html").render()

                for number in range(0,integer_limit):
                    list_final_species.append(list_species[number])

                context["length"] = len(list_species)
                context["species_list"] = list_final_species
                if "json" in arguments or chk:
                    contents = json.dumps(context)
                    content_type = "application/json"
                else:
                    contents = read_template_html_file("list_species.html").render(context=context)
            except:
                    contents = read_template_html_file("error.html").render()



        elif path_name == "/karyotype":
            try:
                species = arguments["specie"][0].replace(" ", "_")
                ENDPOINT = "info/assembly/" + species
                connection = http.client.HTTPConnection(SERVER)
                connection.request("GET", ENDPOINT + PARAMS)
                response = connection.getresponse().read().decode()
                dictionary_response = json.loads(response)
                karyotype = dictionary_response.get("karyotype")
                context["list_karyotype"] = karyotype
                if "json" in arguments:
                    contents = json.dumps(context)
                    content_type = "application/json"
                else:
                    contents = read_template_html_file("karyotype.html").render(context=context)

            except:
                contents = read_template_html_file("error.html").render()


        elif path_name == "/chromosomeLength":
            try:
                species = arguments["specie"][0].replace(" ", "_")
                ENDPOINT = "info/assembly/" + species
                connection = http.client.HTTPConnection(SERVER)
                connection.request("GET", ENDPOINT + PARAMS)
                response = connection.getresponse().read().decode()
                dictionary_response = json.loads(response)
                list_possible_values = dictionary_response["top_level_region"]
                new_list = []
                for dictionaries in list_possible_values:
                    if "chromosome" in dictionaries.values():
                        new_list.append(dictionaries)
                user_chromosome = arguments["chromo"][0]
                user_chromosome = user_chromosome.upper()
                for dictionary in new_list:
                    if dictionary["name"] == user_chromosome:
                        length = dictionary["length"]

                context["length_chromosome"] = length
                if "json" in arguments:
                    contents = json.dumps(context)
                    content_type = "application/json"
                else:
                    contents = read_template_html_file("chromosome.html").render(context=context)
            except:
                contents = read_template_html_file("error.html").render()

        elif path_name == "/geneSeq":
            try:
                gene = arguments["gene"][0]
                value_gene = DICT_GENES[gene]
                ENDPOINT = "sequence/id/" + value_gene
                connection = http.client.HTTPConnection(SERVER)
                connection.request("GET", ENDPOINT + PARAMS)
                response = connection.getresponse().read().decode()
                dictionary_response = json.loads(response)
                seq = dictionary_response["seq"]
                context["seq"] = seq
                if "json" in arguments:
                    contents = json.dumps(context)
                    content_type = "application/json"
                else:
                    contents = read_template_html_file("gene_sequence.html").render(context=context)

            except:
                contents = read_template_html_file("error.html").render()

        elif path_name == "/geneInfo":
            try:
                gene = arguments["gene_info"][0]
                value_gene = DICT_GENES[gene]
                ENDPOINT = "sequence/id/" + value_gene
                connection = http.client.HTTPConnection(SERVER)
                connection.request("GET", ENDPOINT + PARAMS)
                response = connection.getresponse().read().decode()
                dictionary_response = json.loads(response)
                seq = dictionary_response["seq"]
                length_sequence = len(seq)
                context["length_sequence"] = length_sequence
                Id = dictionary_response["id"]
                context["ID"] = Id
                chromosome_name = dictionary_response["desc"]
                final_chromosome_name = chromosome_name.split(":")
                context["start"] = final_chromosome_name[3]
                context["end"] = final_chromosome_name[4]
                context["chromosome_name"] = final_chromosome_name[1]
                if "json" in arguments:
                    contents = json.dumps(context)
                    content_type = "application/json"
                else:
                    contents = read_template_html_file("gene_info.html").render(context=context)

            except:
                contents = read_template_html_file("error.html").render()

        elif path_name == "/geneCalc":
            try:
                gene = arguments["gene_calculations"][0]
                value_gene = DICT_GENES[gene]
                ENDPOINT = "sequence/id/" + value_gene
                connection = http.client.HTTPConnection(SERVER)
                connection.request("GET", ENDPOINT + PARAMS)
                response = connection.getresponse().read().decode()
                dictionary_response = json.loads(response)
                seq = dictionary_response["seq"]
                total = len(seq)
                a, c, g, t = 0, 0, 0, 0
                for base in seq:
                    if base == "C":
                        c += 1
                    elif base == "G":
                        g += 1
                    elif base == "A":
                        a += 1
                    elif base == "T":
                        t += 1
                context["percentage_a"] = round((a / total) * 100, 3)
                context["percentage_c"] = round((c / total) * 100, 3)
                context["percentage_g"] = round((g / total) * 100, 3)
                context["percentage_t"] = round((t / total) * 100, 3)
                context["total_length"] = total
                if "json" in arguments:
                    contents = json.dumps(context)
                    content_type = "application/json"
                else:
                    contents = read_template_html_file("gene_calculations.html").render(context=context)
            except:
                contents = read_template_html_file("error.html").render()

        else:
            contents = read_template_html_file("error.html").render()



        self.send_response(200)  # Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


    # Server MAIN program

    # Set the new handler
Handler = TestHandler

    # Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)
    print("Waiting for server")

        # Main loop: Attend the client. Whenever there is a new client, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()