def indexOfPeakEle(arr,n):
    # if length of arr is 1 then return index 0
    if n == 0:
        return 0

    # check if the first or last element is peak ?
    if arr[0] >= arr[1]:
        return 0

    if arr[n-1] >= arr[n-2]:
        return n-1

    # check the left elements in arr
    for i in range(1,n-1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            return i
        return -1

    # fetch index
    
    


def main():
    arr = [1,2,10,3,8,5,3,9]
    n = len(arr)
    index = indexOfPeakEle(arr,n)
    if index != -1 and (index == 0 or arr[index]>= arr[index-1]) and (index == n-1 or arr[index] >= arr[index+1]):
        print(1)
    else:
        print(0)
main()