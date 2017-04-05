

def aggregate(data, dataDict):
    magic = data[0]
    if (validateMagic(magic)):
        id = data[1]
        funcType = data[2]
        storageType = data[3]
        sequence = data[4]
        payloadLength = data[5]
        payload = []
        for x in range(0,payloadLength):
            payload.append(data[x])
        dataRep = dataDict[id]
        if dataRep is None:
            payloads = []
            payloads.insert(sequence, payload)
            dataRep = {'function' : getFunction(funcType), 'storageType' : storageType, 'payloads' : payloads}
        else:
            payloads = dataRep['payloads']
            payloads.insert(sequence, payload)
            dataRep['payloads'] = payloads
        dataDict[id] = dataRep

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
        "Unknown"
