# def prefixSum(arr):
#     s = []
#     a = 0
#     for i in range(0,len(arr)):
#         a += i


# def main():
#     arr = [-3,2,9,8,-3,5,2,1]
#     n = len(arr)
#     queries = [[0,6],[2,5],[1,4],[3,7]]
#     ans = prefixSum(arr,queries)
#     ps=[]
#     ps.append(s)
# main()



def main():
    arr = [-3,2,9,8,-3,5,2,1]
    n = len(arr)
    queries = [[0,6],[2,5],[1,4],[3,7]]
    prefixSum = [0 for i in range(n)]
    
    for i in range(n):
        if i == 0: prefixSum[i] = arr[i]     
        else: prefixSum[i] = prefixSum[i-1]+arr[i]

    for query in queries:
        si = query[0]
        ei = query[1]
        if si == 0 :
            print(prefixSum[ei],end= " ")
        else:
            print(prefixSum[ei] - prefixSum[si-1],end=" ")
main()


