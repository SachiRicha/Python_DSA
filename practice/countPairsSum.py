def sumPairs(arr,k):
    # start = 0
    # end = 1
    # count = 0
    # n = len(arr)
    # for i in range(n-1):
    #     for j in range(i+1, n):
    #         if arr[i] + arr[j] == k:
    #             count+=1
    #     # while end!=len(arr)-1:
    #     #     if arr[i] + arr[end] == k:
    #     #         count+=1
    #     #         end+=1
    #     #     return 0
    # return count
    freq = {}
    count = 0
    
    for num in arr:
        target = k - num
        if target in freq:
            count += freq[target]
        
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    return count
        

def main():
    arr = [1,1,1,1]
    k = 2
    print(sumPairs(arr,k))
main()