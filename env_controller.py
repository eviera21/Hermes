from client import EchoClient
from server import EchoServer
import requests, logging

logging.basicConfig(filename= "env_logs.log", level=logging.DEBUG, format='%(name)s: %(message)s')

class EnvController:
    #Object to control the language environment
    def __init__(self):
        self.logger = logging.getLogger('EnvController')
        self.env = dict()

    def create_server(self, server_name, ip, port):
        #Set new server to the environment. If port = 0, then kernel will take care of the port
        the_ip = ip
        the_port = port

        var_ip = self.verify_var(ip)

        if(var_ip):
            the_ip = var_ip

        try:
            address = (the_ip,the_port)
            new_server = EchoServer(address)
            new_server.run_me()
            self.env[server_name] = new_server
        except Exception as e:
            if(isinstance(e, TypeError)):
                print(f'Error: Unrecognized variable.')
            if(isinstance(e, OSError)):
                print(f'Error: {e}.')

    def create_client(self, client_name):
        # Set or update client to the environment.
        if(self.verify_var(client_name)):
            print(f'Error: client with the name \"{client_name}\" already exists.')
            return
        self.env[client_name] = EchoClient()

    def delete_client_or_server(self, var_name):
        # remove server or client frrmo environment.
        value = self.verify_var(var_name)
        if(isinstance(value, EchoServer)):
            value.stop_me()
            removed_server = self.env.pop(var_name)
            self.logger.debug(f'server removed: server_id={removed_server.id}')
            return removed_server
        elif(isinstance(value, EchoClient)):
            removed_client = self.env.pop(var_name)
            self.logger.debug(f'client removed: client_id={removed_client.id}')
            return removed_client
        elif(isinstance(value, (int, str))):
            print(f'Error: Variable {var_name} isnot of type: \"EchoServer\" or \"EchoClient\"')
        else:
            print(f'Error: Unrecognized variable \"{var_name}\"')

    def var_assign(self, var_name, value):
        if(not isinstance(value, (str, int))):
            print(f'Unassigned variable: value must be integer or string')
            return
        self.env[var_name] = value

    def send_messsage(self, sender, receiver, message):
        the_sender = self.verify_var(sender)
        the_receiver = self.verify_var(receiver)
        if(not the_sender):
            print(f'Error: Unassigned variable {sender}=None')
            return
        if(not the_receiver):
            print(f'Error: Unassigned receiver {receiver}=None')
            return
        if(isinstance(the_sender, EchoClient) and isinstance(the_receiver,EchoServer)):
            s1 : EchoServer = the_sender
            s2 : EchoServer = the_receiver
            s1.message_peer(message, s2)

    def info(self, var_name):
        something = self.verify_var(var_name)
        if(something):
            print(something)
        else:
            print(f'Error: Unrecognized variable: {var_name}')

    def connect_external(self, sender, external_address):
        the_sender = self.verify_var
        the_external_address = external_address
        tmp_var = self.verify_var(external_address)
        if(isinstance(the_sender, (EchoClient, EchoServer))):
            the_sender.send_external(external_address)
        else:
            print(f'Error: Variable is not type \"EchoServer\" or \"EchoClient\"')

    def verify_var(self, var):
        try:
            return self.env[var]
        except KeyError:
            return None

    def __repr__(self):
        return self.env

