import socket
import signal
import sys
import psutil   #pip install psutil

def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

##

ip_addr = "127.0.0.1"
tcp_port = 1005
count=0

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((ip_addr, tcp_port))

while True:
    while(count%40000000 == 0): #4 in 4 second sending data
        try: 
            cpu = "CPU utilization: " + str(psutil.cpu_percent()) + "%"         # gives a single float value
            memory = psutil.virtual_memory()                                    # gives an object with many fields
            dic = "Percentage of memory in use: " + str(dict(psutil.virtual_memory()._asdict())['percent']) + "%" #Converted to a dictionary to can print easier

            sock.send((cpu).encode())
            sock.send((dic).encode())
            response = sock.recv(4096).decode()
            print('\nServer response: {}'.format(response))
            count+=1
            
        except (socket.timeout, socket.error):
            print('Server error. Done!')
            sys.exit(0)
    count+=1

