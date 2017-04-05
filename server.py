import bluetooth

hostMACAddress = 'B8:27:EB:10:0B:97' # The MAC address of a Bluetooth adapter on the Raspberry Pi found using "sudo hciconfig" on RPi.
port = 3
backlog = 1
size = 1024

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)

try:
    client, clientInfo = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            print(data)
            client.send(data) # Echo back to client
except:	
    print("Closing socket")
    client.close()
    s.close()