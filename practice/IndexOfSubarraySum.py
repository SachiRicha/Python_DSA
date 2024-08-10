def indexOfSubarraySum(arr,n,s):
    start = 0
    curr_sum = 0
    for i in range(n):
        curr_sum=curr_sum+arr[i]
        while curr_sum > s and start <= i:
            curr_sum -= arr[start]
            start+=1
        if curr_sum == s:
            return [start+1,i+1]
    return -1


def main():
    arr = [1,2,3,4,5,6,7,8,9,10]
    n = len(arr)
    s = 15
    print(indexOfSubarraySum(arr,n,s))
main()