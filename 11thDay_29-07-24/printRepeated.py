def frequencyNumber(arr,k):
    arr.sort()
    # occurance = {num:arr.count(num) for num in arr}
    # return occurance
    _map = []
    j = len(arr)-1
    while j>=0:
        if arr[j] in _map:
            continue

        n=arr[j]
        c = 0
        i =j
        while k>0:
            k = k - (arr[j] - arr[i])
            c+=1
            i-=1
        ans = max(ans,c)

    


def main():
    arr = [1,1,1,9,1,3,3,15,3,1,1]
    k = 5
    print(frequencyNumber(arr,k))
main()