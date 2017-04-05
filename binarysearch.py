def binary_search(arr,value):
    left = 0
    right = len(arr) - 1
    while(left <= right):
        mid = (left + right) // 2
        print(mid)
        if arr[mid] is value:
            return mid
        elif value < arr[mid]:
            right = mid - 1
        elif value > arr[mid]:
            left = mid + 1

    return -1

def print_binary_search(arr,value):
    pos = binary_search(arr,value)
    if pos is -1:
        print("Element not found")
    else:
        print("Element found in the positon " +str(pos))



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
