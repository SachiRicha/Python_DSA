nums = [3,3]
target = 6
targetSumIndex = []
# for i in range(len(nums)-1):
#     sum = nums[i] + nums[i+1]
#     targetSumIndex.append(sum)
#     # print(i,i+1)
#     if sum == target:
#         print(i,i+1)
#         break

for i in range(len(nums)-1):
    numTarget = target - nums[i]
    if numTarget in nums:
        print(i,nums.index(numTarget))