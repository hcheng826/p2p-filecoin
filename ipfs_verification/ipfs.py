import socket
import os
import time

class Owner():
    def __init__(self, host_port_list=[]):
        self.host_port_list = host_port_list
        self.minerList = []

    def add_file(self, filename):
        add_log = os.popen('ipfs add %s' %filename).read()
        print(add_log)
        self.filename = filename
        self.hash_value = add_log.split()[1]
        self.request_pin()
    
    def get_file(self, filename):
        os.system('ipfs get %s -o %s'%(self.hash_value, filename))
    
    def request_pin(self):
        for host, port in self.host_port_list:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host, port))
            client.send(('pin %s'%self.hash_value).encode())
            data = client.recv(1024)
            self.add_miner(data.decode())
    
    def add_miner(self, miner_ipfs_id):
        self.minerList.append(miner_ipfs_id)

    def get_filecheck_ans(self, token):
        filehash_log = os.popen('go run file_hash.go %s %s'%(self.filename, token)).read()
        return filehash_log

    def miner_filecheck(self):
        token = time.time()
        filehash_ans = self.get_filecheck_ans(token)
        for host, port in self.host_port_list:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host, port))
            client.send(('check %s %s'%(self.hash_value, token)).encode())
            data = client.recv(1024)
            print('hash from my file: %s'%filehash_ans)
            print('hash from miner:   %s'%data.decode())
            if filehash_ans == data.decode():
                print('good miner')
            else:
                print('bad miner')

class Miner():
    def __init__(self, host, port, ipfs_id):
        self.host = host
        self.port = port
        self.ipfs_id = ipfs_id

    def pin_file(self, hash_value):
        os.system('ipfs get %s'%hash_value)
        os.system('ipfs pin add %s'%hash_value)

    def get_filecheck_ans(self, hash_value, token):
        filehash_log = os.popen('go run file_hash.go %s %s'%(hash_value, token)).read()
        return filehash_log

    def listen(self):
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serv.bind((self.host, self.port))
        serv.listen(5)
        while True:
            (csock, adr) = serv.accept()
    
            data = csock.recv(1024)
            content = data.decode().split()
            print(content)
            if content[0] == 'pin':
                self.pin_file(content[1])
                csock.send(self.ipfs_id.encode())
            elif content[0] == 'check':
                ans = self.get_filecheck_ans(content[1], content[2])
                csock.send(ans.encode())

class BadMiner():
    def __init__(self, host, port, ipfs_id):
        self.host = host
        self.port = port
        self.ipfs_id = ipfs_id

    def pin_file(self, hash_value):
        os.system('ipfs get %s'%hash_value)
        os.system('ipfs pin add %s'%hash_value)

    def get_filecheck_ans(self, hash_value, token):
        filehash_log = os.popen('go run file_hash.go %s %s'%(hash_value, token)).read()
        return filehash_log

    def listen(self):
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serv.bind((self.host, self.port))
        serv.listen(5)
        while True:
            (csock, adr) = serv.accept()
    
            data = csock.recv(1024)
            content = data.decode().split()
            print(content)
            if content[0] == 'pin':
                #self.pin_file(content[1])
                csock.send(self.ipfs_id.encode())
            elif content[0] == 'check':
                ans = self.get_filecheck_ans(content[1], content[2])
                csock.send(ans.encode())

if __name__ == '__main__':
    pass
