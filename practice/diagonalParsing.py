def parseDiagonal(arr):
    i = 0
    j = 0
    n = len(arr)
    while j < n:
        cj = j
        while cj <n:
            print(arr[i][cj],end=" ")
            i+=1
            cj+=1
        print()
        i = 0
        j += 1

def main():
    arr = [[3,9,-1,3,2],[0,2,8,-1,5],[0,0,6,6,7],[0,0,0,5,8],[0,0,0,0,3]]
    parseDiagonal(arr)
    
main()