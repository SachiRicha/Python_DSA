def missingEle(arr,n):  
    return int(n*(n+1)/2 - sum(arr))


def main():
    arr = [1,2,3,5]
    n = 5
    print(missingEle(arr,n))
main()