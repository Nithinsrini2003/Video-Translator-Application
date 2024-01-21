import socket


# Initialize Socket Instance
sock = socket.socket()
print ("Socket created successfully.")

# Defining port and host
port = 8800
host = 'localhost'

# Connect socket to the host and port
sock.connect((host, port))
print('Connection Established.')
# Send a greeting to the server
sock.send('A message from the client'.encode())

# Write File in binary
file = open('client-file.txt', 'wb')

# Keep receiving data from the server
line = sock.recv(1024)

while(line):
    file.write(line)
    line = sock.recv(1024)

print('File has been received successfully.')

file.close()
sock.close()
print('Connection Closed.')

# Initialize Socket Instance
sock = socket.socket()
print ("Socket created successfully.")

# Defining port and host
port = 8800
host = ''

# binding to the host and port
sock.bind((host, port))

# Accepts up to 10 connections
sock.listen(10)
print('Socket is listening...')

while True:
    # Establish connection with the clients.
    con, addr = sock.accept()
    print('Connected with ', addr)

    # Get data from the client
    data = con.recv(1024)
    print(data.decode())
    # Read File in binary
    file = open('matti.mp4', 'rb')
    line = file.read(1024)
    # Keep sending data to the client
    while(line):
        con.send(line)
        line = file.read(1024)
    
    file.close()
    print('File has been transferred successfully.')

    con.close()