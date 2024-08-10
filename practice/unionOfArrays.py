def unionOfArrays(arr1,arr2):
    s1 = set(arr1)
    s2 = set(arr2)
    return len(s1.union(s2))
    

def main():
    arr1 = [1,2,3,4,5]
    arr2 = [1,2,3]
    print(unionOfArrays(arr1,arr2))
main()