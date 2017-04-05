import bluetooth
import protocol

hostMACAddress = 'B8:27:EB:9B:8B:74' # The MAC address of a Bluetooth adapter on the Raspberry Pi found using "sudo hciconfig" on RPi.
port = 3
backlog = 1
size = 1024

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_socket.bind((hostMACAddress,port))
server_socket.listen(backlog)
print("listening")
dataDict = {}

try:
    client, clientInfo = server_socket.accept()
    print("accepting")
    while 1:
        print("receiving")
        data = client.recv(size)
        if data is None:
            print("no data")
        elif data is not None:
            protocol.aggregate(data, dataDict)
            print(data)
            client.send(data) # Echo back to client.
        
        
except:
    print("Closing socket")
    client.close()
    server_socket.close()
