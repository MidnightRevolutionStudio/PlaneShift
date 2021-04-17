from http.server import BaseHTTPRequestHandler, HTTPServer
import ServerSender
import json

current_sessions = []

def PostToUsers(dataObj, sender_ip: str, route: str, body: str):
    if sender_ip == dataObj["host"]["IP"]:
        for i in range(len(dataObj["players"])):
            ServerSender.Post(dataObj["players"][i]["IP"], 1138, route, body)
    else:
        ServerSender.Post(dataObj["host"], 1138, route, body)
        for i in range(len(dataObj["players"])):
            if(dataObj["players"][i] != sender_ip):
                ServerSender.Post(dataObj["players"][i]["IP"], 1138, route, body)
    


def GetRequestEnging(req: BaseHTTPRequestHandler):
    if(req.path == "/"):
        req.send_response(200)
        req.send_header('Content-Type', 'text/html')
        req.send_header('youre header', 42)
        req.end_headers()

        message = "Welcome, master"
        req.wfile.write(bytes(message, "utf8"))
    elif(req.path == "/testClient"):
        response = ServerSender.ServerSendGet("localhost", 1138, "/")
        req.send_response(200)
        req.send_header('Content-Type', 'text/html')
        req.end_headers()

        message = response
        req.wfile.write(bytes(message, "utf8"))
    elif(str.startswith(req.path, "/CreateSession")):
        usr_Name = req.path.split("/")[2]
        current_sessions.append({ "host" : { "UserName": usr_Name, "IP" : req.client_address[0]}, "players" : [] })

        req.send_response(201)
        req.send_header('Content-Type', 'text/html')
        req.end_headers()

        message = "Your game is created for your IP " + req.client_address[0]
        req.wfile.write(bytes(message, "utf8"))
    elif(str.startswith(req.path, "/CloseSession")):
        usr_Name = req.path.split("/")[2]
        found_session = False
        for i in range(len(current_sessions)):
            if(current_sessions[i]["host"]["IP"] == req.client_address[0] and current_sessions[i]["host"]["UserName"] == usr_Name):
                found_session = True
                current_sessions.pop(i)
                pass
        if(not found_session):
            req.send_response(404)
            req.send_header('Content-Type', 'text/html')
            req.end_headers()

            message = "Could not find session to close for user: " + usr_Name
            req.wfile.write(bytes(message, "utf8"))
        else:
            req.send_response(200)
            req.send_header('Content-Type', 'text/html')
            req.end_headers()

            message = "Successfully closed session for " + usr_Name
            req.wfile.write(bytes(message, "utf8"))

def PostRequestEngine(req: BaseHTTPRequestHandler):
    print("post requset sent from " + req.client_address[0])
    content_len = int(req.headers.get('Content-Length'))
    post_body = req.rfile.read(content_len)
    body = json.loads(post_body)
    if(req.path == "/SendCharacter"):
        found_session = False
        for i in range(len(current_sessions)):
            if current_sessions[i]["host"]["IP"] == req.client_address[0] or req.client_address[0] in current_sessions[i]["players"]:
                found_session = True
                PostToUsers(current_sessions[i], req.client_address[0], "/SendCharacter", post_body)
        if(not found_session):
            req.send_response(404)
            req.send_header('Content-Type', 'text/html')
            req.end_headers()

            message = "Could not find session you belong to"
            req.wfile.write(bytes(message, "utf8"))
        else:
            req.send_response(200)
            req.send_header('Content-Type', 'text/html')
            req.end_headers()

            message = "You sent the character to all people in the session"
            req.wfile.write(bytes(message, "utf8"))
    
    elif(str.startswith(req.path, "/JoinSession")):
        host_usr = body["HostUser"]
        found_session = False
        for i in range(len(current_sessions)):
            if(current_sessions[i]["host"]["UserName"] == host_usr):
                found_session = True
                current_sessions[i]["players"].append({"UserName" : body["PlayerUser"], "IP" : req.client_address[0]})
                pass

        if(not found_session):
            req.send_response(404)
            req.send_header('Content-Type', 'text/html')
            req.end_headers()

            message = "Could not find session for user: " + host_usr
            req.wfile.write(bytes(message, "utf8"))
        else:
            req.send_response(200)
            req.send_header('Content-Type', 'text/html')
            req.end_headers()

            message = "You have joined " + host_usr + "'s session"
            req.wfile.write(bytes(message, "utf8"))