from http.server import BaseHTTPRequestHandler, HTTPServer
import client

current_sessions = []

def GetRequestEnging(req: BaseHTTPRequestHandler):
    if(req.path == "/"):
        req.send_response(200)
        req.send_header('Content-Type', 'text/html')
        req.send_header('youre header', 42)
        req.end_headers()

        message = "Welcome, master"
        req.wfile.write(bytes(message, "utf8"))
    elif(req.path == "/testClient"):
        response = client.ServerSend("localhost", 1138)
        req.send_response(200)
        req.send_header('Content-Type', 'text/html')
        req.end_headers()

        message = response
        req.wfile.write(bytes(message, "utf8"))
    elif(req.path == "/CreateSession"):
        current_sessions.append({ "host_ip" : req.client_address, "players" : [] })

        req.send_response(201)
        req.send_header('Content-Type', 'text/html')
        req.end_headers()

        message = "Your game is created for your IP " + req.client_address
        req.wfile.write(bytes(message, "utf8"))
    elif(str.startswith(req.path, "/JoinSession")):
        host_ip = req.path.split("/")[1]

        found_session = False
        for i in range(len(current_sessions)):
            if(current_sessions[i]["host_ip"] == host_ip):
                found_session = True
                current_sessions[i]["players"].append(req.client_address)
                pass

        if(not found_session):
            req.send_response(404)
            req.send_header('Content-Type', 'text/html')
            req.end_headers()

            message = "Could not find session at ip: " + host_ip
            req.wfile.write(bytes(message, "utf8"))
        else:
            req.send_response(200)
            req.send_header('Content-Type', 'text/html')
            req.end_headers()

            message = "You have joined the session at ip: " + host_ip
            req.wfile.write(bytes(message, "utf8"))
    elif(req.path == "/CloseSession"):
        found_session = False
        for i in range(len(current_sessions)):
            if(current_sessions[i]["host_ip"] == req.client_address):
                found_session = True
                current_sessions.pop(i)
                pass
        if(not found_session):
            req.send_response(404)
            req.send_header('Content-Type', 'text/html')
            req.end_headers()

            message = "Could not find session to close for ip: " + req.client_address
            req.wfile.write(bytes(message, "utf8"))
        else:
            req.send_response(200)
            req.send_header('Content-Type', 'text/html')
            req.end_headers()

            message = "Successfully closed session at ip: " + req.client_address
            req.wfile.write(bytes(message, "utf8"))
