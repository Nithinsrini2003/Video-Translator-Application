import socket
import time


def send_file(filename, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sender_socket:
        sender_socket.connect((host, port))
       
        with open(filename, 'rb') as file:
            sender_socket.sendfile(file, 0)


filename = r"C:\Users\DELL\Desktop\CN Projects\video.mp4" # Replace with your video file's path using raw string
host = '172.20.10.5'  # Change this to the destination computer's IP address
port = 12345  # Change this to an available port

send_file(filename, host, port)

#transfer_time = send_file(filename, host, port)
#print(f"Transfer Time: {transfer_time} seconds")



#172.20.10.5