

def aggregate(data, dataDict):
    magic = data[0]
    if validateMagic(magic):
        id = data[1]
        funcType = data[2]
        storageType = data[3]
        sequence = data[4]
        payloadLength = data[5]
        payload = []
        print(str(payloadLength))
        for x in range(6,payloadLength + 6):
            payload.append(data[x])
        print("payload %s", payload)
        dataRep = dataDict.get(id)
        if dataRep is None:
            payloads = []
            payloads.insert(sequence, payload)
            dataRep = {'function' : getFunction(funcType), 'storageType' : storageType, 'payloads' : payloads}
        else:
            payloads = dataRep['payloads']
            payloads.insert(sequence, payload)
            dataRep['payloads'] = payloads
        dataDict[id] = dataRep
        lastByte = payload[len(payload) - 1]
        if lastByte == 0x0A:
            process(dataDict, id)
    else:
        print("Incorrect Magic")

def process(dataDict,id):
    dataRep = dataDict[id]
    #TODO: process data based on function
    return True


def validateMagic(magic):
    if magic == 0xFA:
        return True
    return False

def getFunction(funcType):
    if funcType == 0x00:
        return "Search"
    elif funcType == 0x01:
        return "Sort"
    elif funcType == 0x02:
        return "Store"
    elif funcType == 0x03:
        return "Retrieve"
    else:
        return "Unknown"

debug = False
if debug:
    dataDict = {}
    data = [0xFA, 0x01, 0x02, 0x01, 0x01, 0x01, 0x0F]
    aggregate(data, dataDict)
    print(dataDict)
    data = [0xFA, 0x01, 0x02, 0x01, 0x01, 0x01, 0x0B]
    aggregate(data, dataDict)
    print(dataDict)
    data = [0xFA, 0x02, 0x02, 0x01, 0x01, 0x01, 0x0F]
    aggregate(data, dataDict)
    print(dataDict)
