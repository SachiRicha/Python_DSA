def buildMatrix(str1,dp):
    si = 0
    ei = 0
    n = len(dp)
    count = 0
    k = 3
    kCount = 0
    largest =""
    smallest = ""
    while ei<n:
        ce=ei
        while ce < n:
            if si == ce:
                dp[si][ce] = 1
                count+=1
                largest = str1[si:ce+1]
                if abs(si-ce) == k-1:
                    kCount+=1
            elif abs(ce-si) <= 2:
                if str1[si] == str1[ce]:
                    dp[si][ce] = 1
                    count += 1
                    largest = str1[si:ce+1]
                    if smallest == "":
                        smallest = str1[si:ce+1]
                    if abs(si-ce) == k-1:
                        kCount+=1
            else:
                if str1[si] == str1[ce] and dp[si+1][ce-1] == 1:
                    dp[si][ce] = 1
                    count+=1
                    largest = str1[si:ce+1]
                    if smallest == "":
                        smallest = str1[si:ce+1]
                    if abs(si-ce) == k-1:
                        kCount+=1
            si+=1
            ce+=1
        si=0
        ei+=1
    return [dp,count,largest,smallest,kCount]


def main():
    str1= "abcdcbcbaudbz"
    n = len(str1)
    dp = [[0 for i in range(n)] for j in range(n)]
   
    ans = buildMatrix(str1,dp)
    dp = ans[0]
    totalNumberOfPalindromeicSubstring = ans[1]
    largest = ans[2]
    smallest = ans[3]
    kCount = ans[4]
    print(totalNumberOfPalindromeicSubstring)
    print(largest)
    print(smallest)
    print(kCount)
    print("dp is:",dp)
main()

