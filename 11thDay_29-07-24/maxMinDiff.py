def maxMin(arr,k):
    maxEle = max(arr)
    minEle = min(arr)
    return (maxEle-k) - (minEle + k)

def main():
    arr = [8,7,3,2,4,5,6]
    k = 3
    print(maxMin(arr,k))
main()