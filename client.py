import logging
import uuid
from server import EchoServer
import socket
import requests

logging.basicConfig(filename= "env_logs.log", level=logging.DEBUG, format='%(name)s: %(message)s')

class EchoClient:
    def __init__(self):
        self.client_id = uuid.uuid4()
        self.logger = logging.getLogger(f'Client({self.client_id})')
        self.connection_history=[]
        self.logger.debug('client created')

    def info(self):
        return self.__repr__()

    def send_external(self, external_address):
        self.logger.debug(f'connecting to {external_address}')
        req = requests.get(url=external_address)
        print(f'Response from {external_address}: {req.status_code}')
        self.connection_history.append(external_address)

    def send_message(self, message, server: EchoServer):
        try:
            self.logger.debug(f'sending message to server = {server.server_id}, message=\"{message}\"')
            self.connection_history.append(server.server_id.__str__())
            ip, port = server.server_address
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.sendall(bytes(message,'ascii'))
            print(f'Client({self.client_id}): {message}')
            response = str(sock.recv(1024), 'ascii')
            sock.close()
            self.logger.debug(f'received response from server={server.server_id}, response={response}')
        except:
            print(f'Yikes, unable to send message to {server}')

    def close_connection(self, server: EchoServer):
        return self.connections.popitem(server)

    def __repr__(self):
        return f'EchoClient>client_id={self.client_id}, connection_history={self.connection_history}>'
