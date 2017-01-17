import SocketServer

class MyUDPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        self.data = self.request[0].strip()
        #print "%s wrote:" % self.client_address[0]
        print self.data

if __name__ == "__main__":
    HOST, PORT = "localhost", 5060

    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)

    server.serve_forever()
