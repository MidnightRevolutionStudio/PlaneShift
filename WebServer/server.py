from http.server import BaseHTTPRequestHandler, HTTPServer
import requestMgr

hostName = "0.0.0.0"
serverPort = 8080

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        #store path and other imeediatelhy usefull information to mgr.
        #mgr parses and sends state updates to appropriate applications
        #mgr returns a status code (and message if needed)
        #handler parses status code and message to return to User
        requestMgr.GetRequestEnging(self)
    def do_POST(self):
        requestMgr.PostRequestEngine(self)

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), handler)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")