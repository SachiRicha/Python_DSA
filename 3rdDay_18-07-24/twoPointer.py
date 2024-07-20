# 2 pointer algorithm

def isPairExist(arr,target):
    arr.sort()
    i=0
    j=len(arr)-1
    while i<j:
        if arr[i]+arr[j] == target: return True
        if arr[i]+arr[j] >target : j-=1
        if arr[i]+arr[j] <target: i+=1
    return False



def main():
    # arr = list(map(int(input().split(','))))
    # target = int(input())
    arr = [3,-2,5,6,9,13,5,-12,8]
    target = 5
    ans = isPairExist(arr,target)
    print(ans)
main()