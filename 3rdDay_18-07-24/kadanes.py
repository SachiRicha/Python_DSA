def maxSum(arr):
    ans = float("-inf")
    ctsum = 0
    for i in range(len(arr)):
        if ctsum <0:
            cts = 0
        ctsum +=arr[i]
        ans = max(ctsum,ans)
    return max(ans,ctsum)
        
        

def main():
    arr = [-2,3,-5,-6,9,2,-3,7,18,6,-5,100]
    ans = maxSum(arr)
    print(ans)
main()