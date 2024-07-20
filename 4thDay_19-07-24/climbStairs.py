# def waysToStep(st):
#     personStart = 0
#     stCount = 0
#     while personStart < st:
#         # 1step
#         personStart+=1
#         stCount+=1
#     print()

    

# def main():
#     steps = 5
#     ans = waysToStep(steps)
#     print(ans)
# main()

def numberOfWaysToClimbStairs(n,dp):
    if dp[n]!=0:
        return dp[n]
    if n<=3:
        return n
    a1 = numberOfWaysToClimbStairs(n-1,dp)
    dp[n-1] = a1 #memorize
    a2 = numberOfWaysToClimbStairs(n-2,dp)
    dp[n-2] = a2    #memorize
    return a1+a2 



def main():
    n = 3
    dp = [0 for i in range(n+1)]
    print(numberOfWaysToClimbStairs(n,dp))
main()