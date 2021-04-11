from http.server import BaseHTTPRequestHandler, HTTPServer

def GetRequestEnging(requestHandler: BaseHTTPRequestHandler):
    if(requestHandler.path == "/"):
        requestHandler.send_response(200)
        requestHandler.send_header('Content-Type', 'text/html')
        requestHandler.send_header('youre header', 42)
        requestHandler.end_headers()

        message = "Welcome, master"
        requestHandler.wfile.write(bytes(message, "utf8"))

