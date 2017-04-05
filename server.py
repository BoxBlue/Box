import bluetooth
import protocol

hostMACAddress = 'B8:27:EB:10:0B:97' # The MAC address of a Bluetooth adapter on the Raspberry Pi found using "sudo hciconfig" on RPi.
port = 3
backlog = 1
size = 1024

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_socket.bind((hostMACAddress,port))
server_socket.listen(backlog)

dataDict = {}

try:
    client, clientInfo = server_socket.accept()
    while 1:
        data = client.recv(size)
        if data:
            protocol.aggregate(data, dataDict)
            print(data)
            client.send(data) # Echo back to client.
except:
    print("Closing socket")
    client.close()
    server_socket.close()
