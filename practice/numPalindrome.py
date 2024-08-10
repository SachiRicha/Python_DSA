# def isPalindrome(n):
#     num = n
#     reverse = 0
#     while num:
#         remainder = num%10
#         reverse = (reverse*10)+remainder
#         num = num//10
#     if reverse == n:
#         return True
#     else:
#         return False


# def isPalindrome(n):
#     if n<0 or (n%10==0 and n!=0):
#         return False
    
#     reversed_half = 0
#     while n > reversed_half:
#         reversed_half = reversed_half*10+n%10
#         n//=10
#     return n == reversed_half or n == reversed_half//10
    


# def main():
#     x = 121
#     print(isPalindrome(x))
# main()


def isPalindrome(n):
    if n<0 or (n%10 == 0 and n == 0):
        return False
    reversed_half = 0
    while n>reversed_half:
        reversed_half = reversed_half*10 + n%10
        n//=10
    return n == reversed_half or n == reversed_half//10



def main():
    x = 242
    print(isPalindrome(x))
main()