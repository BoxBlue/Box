from bluetooth import *

import protocol

backlog = 1
size = 1024


def runServer():
    server_socket = BluetoothSocket(RFCOMM)
    server_socket.bind(("",PORT_ANY))
    server_socket.listen(backlog)
    print("listening")
    dataDict = {}
    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    advertise_service(server_socket, "BoxBlue",
                            service_id = uuid,
                            service_classes = [ uuid, SERIAL_PORT_CLASS ],
                            profiles = [ SERIAL_PORT_PROFILE ]
                     )

    try:
        print("waiting to accept")
        client, clientInfo = server_socket.accept()
        print("accepting from %s",clientInfo)
        while 1:
            print("receiving")
            data = client.recv(size)
            if data is None:
                print("no data")
            elif data is not None:
            #protocol.aggregate(data, dataDict)
                retVal = protocol.aggregate(data, dataDict)
                if retVal is not None:
                    print("responding with " + str(retVal))
                    client.send(str(retVal)) # Echo back to client.
                else:
                    print("No retval")
    except Exception as err:
        print("Closing socket:",err)
        server_socket.close()
        runServer()

runServer()
