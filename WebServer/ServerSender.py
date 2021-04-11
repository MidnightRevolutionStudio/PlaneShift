import http.client
import json

def ServerSendGet(server: str, port: int, route : str):

    conn = http.client.HTTPConnection(server, port)
    headers = { 'Content-type' : 'application/json' }

    conn.request('GET', '/',headers=headers)
    response = conn.getresponse().read().decode()
    print(server + " sent back " + response)
    return response
def Post(server: str, port: int, route: str, body: str):
    conn = http.client.HTTPConnection(server, port)
    headers = {'Content-type' : 'application/json'}

    conn.request('POST', route, body = body, headers = headers)
    response = conn.getresponse().read().decode()
    print(server + " sent back " + response)
    return response