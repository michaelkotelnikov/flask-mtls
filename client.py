#! /bin/python3

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
client_cert = ('certificates/client/client.pem', 'certificates/client/client.key')
ssl_server = 'https://127.0.0.1:5000'
r = requests.get(ssl_server, cert=client_cert, verify=False)
print(r.text)
