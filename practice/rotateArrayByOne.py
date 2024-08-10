def rotateArr(arr,n):
    l=[]
# 1st method
    # start = 0
    # temp = arr[-1]
    # arr.remove(arr[-1])
    # l[:] = temp + arr
    # return l
# 2ND METHOD

    # arr1 = []
    # arr1[:] = [arr[-1]] + arr[0:len(arr)-1]
    # return arr1

# 3RD METHOD
    # l.append(arr[-1])
    # for i in range(n-1):
    #     l.append(arr[i])
    # return l

# 4TH METHOD
    if not arr:
            return arr
        
        # Rotate the array by one position clockwise
        last_element = arr[-1]
        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = last_element
        
        return arr
        





def main():
    arr = [1,2,3,4,5]
    n = len(arr)
    print(rotateArr(arr,n))
main()