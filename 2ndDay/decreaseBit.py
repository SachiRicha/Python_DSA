
# arr = [4,7,9,17,5,19,3,6];
# wholeXor = 0
# for e in arr : wholeXor = wholeXor^e
# # print(wholeXor)
# if wholeXor == 0:
#     print("Whole XOR of given array is 0.")
# else:
#     for i in arr:
#         for j in arr:
#             a=0
#             if(i!=j):
#                 a = a^j
#                 print(a)

            
    # print(i-wholeXor)
    # for i in arr: wholeXor = wholeXor ^ arr[i]
    

# arr = [4,7,9,17,5,19,3,6];
# wholeXor = 0
# for e in arr : wholeXor = wholeXor^e
# print(wholeXor)
# for i in arr : leftXorExceptI = wholeXor^i
# print(leftXorExceptI)

def getMinimumNumberOfOps(arr):
    wholeXor = 0
    for e in arr : wholeXor = wholeXor ^ e
    ans = float('+inf')
    for e in arr:
        wholeXorExceptE = wholeXor ^e
        if wholeXorExceptE >e:
            continue
        else:
            currAns = e-wholeXorExceptE
            if currAns < ans:
                ans = currAns
    if ans == float('+inf'):
        return -1
    return ans

def main():
    arr = [4,7,9,17,5,19,3,6];
      
    ans = getMinimumNumberOfOps(arr)
    print(ans)

main()



    
    

