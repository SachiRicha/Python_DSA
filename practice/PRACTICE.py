# find duplicates from an array
# def dupEle(arr,n):
#     arr.sort()
#     dup=[]
#     for i in range(n):
#         if arr[i] == arr[i-1] and (i==0 or arr[i] != arr[i-2]):
#             dup.append(arr[i])
#     if not dup:
#         return [-1]
#     return dup


# def main():
#     arr = [0,3,1,2,3,4,7,8,4,7,9,10,10,10,9,34,32,67,34,67]
#     n = len(arr)
#     print(dupEle(arr,n))
# main()

# sort array with respect to height
# names = ['Alice','Bob','Bob']
# heights = [155,185,150]
# l1 = list(zip(names,heights))
# print(l1)
# sortedArr = sorted(l1,key = lambda x:x[1],reverse = True)
# print(sortedArr)
# keys = [i[0] for i in sortedArr]
# print(keys)

# 2nd method :

# names = ['Alice','Bob','Bob']
# heights = [155,185,150]
# combine = list(zip(names,heights))
# combine.sort(reverse = True,key = lambda x:x[1])
# sorted_names = []
# index = 0
# while index<len(combine):
#     name,height = combine[index]
#     sorted_names.append(name)
#     index+=1
# print(sorted_names)


# traversing the array
# def sufficientFoodForRat(arr,n,r,unit):
#     required_food = r*unit
#     sum_Food = 0
#     count = 0 
#     if n == 0:
#         return -1
#     for i in range(n):
#         if sum_Food >= required_food:
#             return count
#         else:
#             sum_Food += arr[i]
#             count += 1
#     if required_food > sum_Food:
#         return 0

# def main():
#     homeNumberArr = [2,8,3,5,7,4,1,2]
#     lenOfHome = len(homeNumberArr)
#     numOfRat = 7
#     unitOfFoodToBeConsumedByRat = 2
#     print(sufficientFoodForRat(homeNumberArr,lenOfHome,numOfRat,unitOfFoodToBeConsumedByRat))
# main()

# bit manipulation

# num = int(input("Enter any number: "))
# print("Enter anyone choice: 1. ON the bit, 2. OFF the bit, 3. TOGGLE the bit")
# ch = int(input("Enter choice: "))
# bitToBeManipulatedIs = int(input("Enter the bit number you want to manipulate: "))
# bitMask = 1<<bitToBeManipulatedIs-1
# if ch == 1:
#     print(f"After ON the {bitToBeManipulatedIs} bit: ",num|bitMask)
# elif ch==2:
#     print(f"After OFF the {bitToBeManipulatedIs} bit: ",num & ~(bitMask))
# elif ch==3:
#     print(f"After TOGGLE the {bitToBeManipulatedIs} bit: ",num ^ bitMask)

# count sum pairs  (AGAIN) :-
# def sumPairs(arr,k):
#     freq = {}
#     count = 0

#     for num in arr:
#         target = k - num
#         if target in freq:
#             count += freq[target]
        
#         if num in freq:
#             freq[num] +=1
#         else:
#             freq[num] = 1
#     return count
    
# def main():
#     arr =[1,1,1,1]
#     k = 2
#     print(sumPairs(arr,k))
# main()

# 3 9 -1 3 2
# 0 2 8 -1 5
# 0 0 6 6 7
# 0 0 0 5 8
# 0 0 0 0 3

# def parseDiagonal(arr,n):
#     i =0
#     j =0
#     while j < n:
#         cj = j
#         while cj < n:
#             print(arr[i][cj],end=" ")
#             i+=1
#             cj+=1
#         print()
#         i = 0
#         j+=1

# def main():
#     arr = [[3,9,-1,3,2],[0,2,8,-1,5],[0,0,6,6,7],[0,0,0,5,8],[0,0,0,0,3]]
#     n = len(arr)
#     parseDiagonal(arr,n)
# main()
    

# reverse the number if leading zero present it should not be printed

def reverseDigit(n):
    rev = 0
    while n!=0:
        rem = n % 10
        if rev == 0 and rem == 0:
            n=n//10
            continue
        rev = rev*10+rem
        n = n//10
    return rev


def main():
    n = int(input("Enter any number: "))
    print(reverseDigit(n))
main()
