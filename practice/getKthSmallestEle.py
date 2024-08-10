def getSmallest(arr,k):
    # 1st method

    arr1 = [0 for i in range(k)]
    for i in range(k):
        arr1[i] = min(arr)
        arr.remove(arr1[i])
    return arr1[-1]

    # 2nd method
    # arr.sort()
    # return arr[k-1]
                
def main():
    arr = [7,10,4,20,15]
    k = 4
    ans = getSmallest(arr,k)
    print(ans)
main()