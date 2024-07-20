def isPalindrome(s):
    if len(s)<=1:
        return True
    if s[0] != s[-1]:
        return False
    else:
       return isPalindrome(s[1:len(s)-1])
    
def main():
    str1 = "papa"
    print(isPalindrome(str1))
main()