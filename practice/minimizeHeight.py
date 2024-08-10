def minimizeHeight(arr,k,n):
    arr1 = []
    for i in range(n):
        if i == 0:
            arr1.append(arr[i] + k)
        else:
            arr1.append(arr[i] - k)
    maxEle = max(arr1)
    print(maxEle)
    minEle = min(arr1)
    print(minEle)
    return maxEle - minEle

def main():
    arr = [3,9,12,16,20]
    k = 3
    n = len(arr)
    print(minimizeHeight(arr,k,n))
main()