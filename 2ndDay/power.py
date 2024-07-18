import math
# num = int(input("Enter any number: "))
# print("power of 2 is :",math.log(num,2))

def powReturn(n):
    if(n &(n-1)==0):
        print("power of 2 is :",math.log(n,2))
        
    return -1

def main():
    dividend = int(input("Enter dividend: "))
    divisor = int(input("enter divisor: "))
    a = powReturn(divisor)
    print(a)
    
main()

