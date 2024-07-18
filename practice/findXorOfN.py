# find xor of 1 to n
# using XOR

# def findXorOfN(n):
#     wholeXor = 0
#     if n ==0:
#         return 0
#     for i in range(1,n+1):
#         wholeXor = wholeXor ^ i
#     return wholeXor



# def main():
#     n = int(input("Enter any number :"))
#     a = findXorOfN(n)
#     print(a)

# main()

# direct approach

def findXorOfNdirect(n):
    if n%4 == 0:
        return n
    if n%4 == 1:
        return 1
    if n%4 == 2:
        return n+1
    if n%4 == 3:
        return 0

def main():
    n = int(input("Enter any number :"))
    a = findXorOfNdirect(n)
    print(a)
main()