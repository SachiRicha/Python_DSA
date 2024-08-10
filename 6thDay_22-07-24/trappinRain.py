arr = [2,0,9,5,7,12]
arr1 = []
for i in arr:


def trap(height):
    ans = 0
    n = len(heights)
    ps = [0 for i in range(n)]
    ss = [0 for i in range(n)]

    for i in range(n):
        if i == 0:
            ps[i] = heights[i]
        else:
            ps[i] = max(ps[i-1],heights[i])
            