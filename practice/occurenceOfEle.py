def numOfOccurence(arr,n,x):
    count = 0
    for i in range(n):
        if arr[i] == x:
            count+=1
    return count


def main():
    arr = [1,1,1,1,1]
    n = len(arr)
    x = 1
    print(numOfOccurence(arr,n,x))
main()