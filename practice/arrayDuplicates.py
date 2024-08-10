def dupArray(arr,n):
    arr.sort()
    dup = []
    count = 0
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            dup.append(arr[i])
    if not dup:
        return [-1]
    return dup

def main():
    arr = [0,3,1,2,3]
    n = len(arr)
    print(dupArray(arr,n))
main()
