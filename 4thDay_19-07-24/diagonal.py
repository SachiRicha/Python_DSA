
# simple way
# arr = [[1,2,3],[0,4,5],[0,0,6]]
# n = len(arr)
# si = 0
# ei = 0
# while ei < n:
#     copyEndIn = ei
#     while copyEndIn < n:
#         print(arr[si][copyEndIn],end=" ")
#         si+=1
#         copyEndIn+=1
#     print()
#     si=0
#     ei+=1

# sir
def diagonalParsing(arr):
    si = 0
    ei = 0
    n = len(arr)
    while ei<n:
        copyEndIn=ei
        while copyEndIn<n:
            print(arr[si][copyEndIn],end=" ")
            si+=1
            copyEndIn+=1
        print()
        si=0
        ei+=1


def main():
    arr = [[3,9,-1,3,2],[0,2,8,-1,5],[0,0,6,6,7],[0,0,0,5,8],[0,0,0,0,3]]
    diagonalParsing(arr)
main()


        
