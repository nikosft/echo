import socket
import sys
import time

address = '10.0.2.4'
port    = 12000
sock    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server  = (address, port )
message = 'Ping'
start = time.time()
sock.connect(server)
sock.sendall(message)
data = sock.recv(1024)
end  = time.time()
print "Received " + data + " after "
print (end - start)
sock.close()
