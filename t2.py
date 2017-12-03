# -*- coding: utf-8 -*-
import socket
import threading
import time


shutdown = False

clients = []

def receving(name, sock):
    global shutdown
    global clients
    while not shutdown:
        try:
            data, addr = sock.recvfrom(1024)

            if "arroirozum" not in str(data):
                print str(data)
            if "Quit" in str(data):
                shutdown = True
            if addr not in clients:
                clients.append(addr)
                s.sendto("arroirozum", addr)
        except:
            pass


host = ''
port = 12001

server = ('172.20.18.20',12000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
#s.setblocking(0)

for i in range(5):
    threading.Thread(target=receving, args=("RecvThread",s)).start()


alias = raw_input("Name: ")
message = alias + " se juntou a conversa"
s.sendto(message, server)
while not shutdown:
    if message == 'Quit':
        shutdown = True
    message = raw_input()
    if message != '':
        for client in clients:
                s.sendto(alias + ": " + message, client)


    time.sleep(0.1)

shutdown = True

s.close()