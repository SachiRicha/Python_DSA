# 1st method

# names = ["Alice","Bob","Bob"]
# heights = [155,185,150]
# l1 = list(zip(names,heights))
# # sorted_d = sorted(d.values(),reverse=True)
# sorted_l1= sorted(l1,key = lambda x:x[1],reverse=True)
# keys = [i[0] for i in sorted_l1]
# print(keys)

# 2nd method

# names = ["Alice","Bob","Bob"]
# heights = [155,185,150]
# combined = list(zip(names,heights))
# combined.sort(reverse=True,key = lambda x:x[1])
# sortedNames=[name for height, name in combined]
# print(sortedNames)

# 3rd method

# names = ["Alice","Bob","Bob"]
# heights = [155,185,150]
# combined = list(zip(names,height))
# combined.sort(reverse=True,key = lambda x:x[1])
# sortedNames=[]
# index = 0
# while index<len(combined):
#     name,height = combined[index]
#     sortedNames.append(name)
#     index+=1
# print(sortedNames)