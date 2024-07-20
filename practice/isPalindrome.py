def isPalindrome(str1):
    if len(str1)<=1:
        return True
    if str1[0] != str1[-1]:
        return False
    return isPalindrome(str1[1:len(str1)-1])

def main():
    stri = input("Enter any string: ")
    ans = isPalindrome(stri)
    if isPalindrome:
        print("Palindrome")
    else:
        print("Not a palindrome")
main()