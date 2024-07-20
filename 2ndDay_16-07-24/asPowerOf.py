def numPowOfTwo(n):
    if n<0:
        return
    powerOfTwo = []
    exponent = 0

    while n>0:
        if n & 1 ==True:
            powerOfTwo.append(2**exponent)
        exponent+=1
        n=n>>1
    print(powerOfTwo)



def main():
    n = int(input("Enter number: "))
    numPowOfTwo(n)

main()