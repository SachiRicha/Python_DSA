import math
num = int(input())
for i in range(math.sqrt(num)):
    if num == i*i:
        print(num," is perfect square.")
    else:
        print("no")
main()


# half way
