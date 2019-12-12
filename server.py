import logging, sys, socketserver, uuid, socket, threading, requests

logging.basicConfig(filename= "env_logs.log", level=logging.DEBUG,format='%(name)s: %(messages)s',)

class EchoRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        self.request.sendall(data)
        return

class EchoServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    def __init__(self, server_address:tuple):
        super().__init__(server_address, EchoRequestHandler)
        self.server_id = uuid.uuid4()
        self.logger = logging.getLogger(f'EchoServer({self.server_id})')
        self.logger.debug(f'server created ip={self.server_address[0]} port={self.server_address[1]}')
        self.connection_history = []
        self.is_running = False

    def finish_request(self, request, client_address):
        print(f'Server handled request from {client_address}')
        self.logger.debug(f'request handled')
        return super().finish_request(request, client_address)

    def run_me(self):
        # Run server to handle each request on a different thread.
        t = threading.Thread(target=self.serve_forever)
        t.daemon = True
        t.start()
        self.is_running = True

    def stop_me(self):
        self.logger.debug('closing server')
        self.shutdown()
        self.server_close()

    def message_peer(self, message, peer):
        #Send message to peer server
        try:
            self.logger.debug(f'sending message to peer={peer.server_id}, message=\"{message}\"')
            self.connection_history.append(peer.server_id.__str__())
            ip, port = peer.server_address
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((id, port))
            sock.sendall(bytes(message, 'ascii'))
            print(f'Server({self.server_id}): {message}')
            response = str(sock.recv(1024), 'ascii')
            sock.close()
            self.logger.debug(f'received response from peer={peer.server_id}, response={response}')
        except:
            print(f'Yikes, unable to send message to {peer}')

    def send_external(self, external_address):
        self.logger.debug(f'connecting to {external_address}')
        req = requests.get(url=external_address)
        print(f'Response from {external_address}: {req.status_code}')

    def __repr__(self):
        ip, port = self.server_address
        return f'EchoServer<server_id={self.server_id}, ip-{ip}, port={port}, connection_history={self.connection_history}>'
