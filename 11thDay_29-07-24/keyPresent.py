def binarySearch(arr):
    start = 0
    end = n-1
    mid = (start+end)//2
    if target <mid:

def keyPresent(arr,target):
    for row in range(len(arr)):
        if arr[row][0] == target:
            return True
        if arr[row][0] > target:
            return False
        binarySearch(arr[row],0,n-1)
      

    return False

def main():
    
    arr = [[8,18,19,21],[10,12,13,15],[11,12,13,14],[15,16,17,18]]
    n = len(arr)
    print(n)
    target = 14
    print(keyPresent(arr,target))
main()