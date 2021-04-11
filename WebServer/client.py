import http.client
import json

def ServerSend(server: str, port: int):

    conn = http.client.HTTPConnection(server, port)
    headers = { 'Content-type' : 'application/json' }

    conn.request('GET', '/',headers=headers)
    response = conn.getresponse().read().decode()
    print(server + " sent back " + response)
    return response