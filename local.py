import platform
import bluetooth

print(platform.machine())

name = "bt_server"
target_name = "siggen"
uuid = "00001101-0000-1000-8000-00805F9B34FB"

def create_server():
    serverSocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = bluetooth.PORT_ANY
    serverSocket.bind(("",port))
    print "Listening for connections on port: ", port   
    serverSocket.listen(1)
    port = serverSocket.getsockname()[1]
    
    #the missing piece
    #advertise_service( server_sock, "SampleServer",
    #                   service_id = uuid,
    #                   service_classes = [ uuid, bluetooth.SERIAL_PORT_CLASS ],
    #                   profiles = [ bluetooth.SERIAL_PORT_PROFILE ] 
    #                    )
    
    inputSocket, address = serverSocket.accept()
    
    print "Got connection with" , address
    data = inputSocket.recv("1024")
    print "received [%s] \n " % data    
    inputSocket.close()
    serverSocket.close()
    
print("Starting server..")
create_server()
print("Complete")