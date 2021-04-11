from http.server import BaseHTTPRequestHandler, HTTPServer
import getMgr

hostName = "localhost"
serverPort = 8080

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        #store path and other imeediatelhy usefull information to mgr.
        #mgr parses and sends state updates to appropriate applications
        #mgr returns a status code (and message if needed)
        #handler parses status code and message to return to User
        getMgr.GetRequestEnging(self)

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), handler)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")