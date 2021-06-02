import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + PARAMS)

response = connection.getresponse()
print(response.status, response.reason)

answer_decoded = response.read().decode()
dict_response = json.loads(answer_decoded)

if dict_response["ping"] == 1:
    print("Ping OK! The database is running.")
else:
    print("DATABASE IS DOWN!")