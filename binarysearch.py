def binary_search(arr,value):
    left = 0
    right = len(arr) - 1
    while(left <= right):
        mid = (left + right) // 2
        print("mid = " + str(mid) + " and target is " + str(value) + "and curr is " + str(arr[mid]))
        curr = int(arr[mid])
        if curr is value:
            return mid
        elif value < curr:
            print("value is less")
            right = mid - 1
        elif value > curr:
            print("value is greater")
            left = mid + 1
    return -1

def print_binary_search(arr,value):
    pos = binary_search(arr,value)
    if pos is -1:
        return "Element not found"
    else:
        return "Element found in the positon " +str(pos)



def test1():
    arr = [2,5,8,9,11,15,17,19,22,26,29,33,56]
    value = 22
    print_binary_search(arr,value)

def test2():
    arr = [2,5,8,9,11,15,17,19,22,26,29,33,56]
    value = 59
    print_binary_search(arr,value)


test1()
test2()
