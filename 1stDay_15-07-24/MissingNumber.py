# n=9;
# arr = [1,3,4,9,6,7,8,5];
# res=0;

# for i in range(1,n+1):
#     res = res ^ i;
# for j in arr:
#     res = res ^ j;
# print(res);

# # class

def getMissingNumber(n,arr):
    ans = 0
    for i in range(1,n+1):
        ans = ans^i;
    for j in arr:
        ans = ans^j;
    return ans


def main():
    n = 10
    arr = [3,2,4,8,9,10,1,5,8,7]
    ans = getMissingNumber(n,arr)
    print(ans)

main()


