def minMaxEle(arr):
    arr1 = []
    arr.sort()
    arr1.append(arr[0])
    arr1.append(arr[-1])
    return arr1
    
def main():
    arr = [56789]
    print(minMaxEle(arr))
main()