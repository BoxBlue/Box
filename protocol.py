import binarysearch
import struct
from PIL import Image
import io
import binascii

def aggregate(data, dataDict):
    data = bytearray(data)
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
        if len(payload) < 255:
            return process(dataDict, id)
    else:
        return "Incorrect Magic"

def process(dataDict,id):
    dataRep = dataDict[id]
    payloads = dataRep['payloads']
    function = dataRep['function']
    if function == 'Search':
        flat = []
        for payload in payloads:
            for x in range(0,len(payload)):
                flat.append(payload[x])
        print("break 1")
        print(flat)
        payloads = bytearray(flat)
        print("break 2")
        payloadsAsStr = str(payloads)
        print("break 3")
        print("payloadsAsStr = " + repr(payloadsAsStr))
        payloadsAsInt = []
        chunk = []
        print("break 4")
        for x in range(0,len(payloadsAsStr)):
            if x is not 0 and x % 4 == 0:
                print("chunk length = " + str(len(chunk)))
                chunk = ''.join(chunk)
                payloadsAsInt.append(struct.unpack(">i",chunk)[0])
                chunk = []
            chunk.append(payloadsAsStr[x])
        target = payloadsAsInt[0]
        vals = payloadsAsInt[1:len(payloadsAsInt)]
        res = binarysearch.print_binary_search(vals,target)
        return res
    elif function == 'Store':
        flat = []
        for payload in payloads:
            payload = bytearray(payload)
            for p in payload:
                flat.append(p)
        #flat is now one big array of all the bytes in image
        r_data = bytes(flat)
        image = Image.open(io.BytesIO(r_data))
        savepath = "~/" + str(id) + "image.bmp"
        res = ""
        try:
            image.save(savepath)
            res = "Image saved"
        except Exception as err:
            res = "Couldn't save image because: " + str(err)
        return res
    elif function == 'Sort':
        flat = []
        for payload in payloads:
            payload = bytearray(payload)
            for p in payload:
                flat.append(p)
        flat.sort()
        return flat

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
