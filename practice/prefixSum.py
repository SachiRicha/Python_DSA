arr = [-3,5,7,9,2,5,-4,7,6]
queries = [[0,5],[3,7],[2,5],[5,7]]
n = len(arr)
prefixSum = [0 for i in range(n)]

for i in range(n):
    if i == 0:
        prefixSum[i] = arr[i]
    else:
        prefixSum[i] = prefixSum[i-1]+arr[i]
print(prefixSum)

for i in queries:
    si = i[0]
    ei = i[1]
    if si == 0:
        print(prefixSum[ei],end=" ")
    else:
        print(prefixSum[ei]-prefixSum[si-1],end=" ")

