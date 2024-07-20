def subsequenceOfArr(arr,index=0,currAns=[]):
    
    if len(arr) == index:
        print(currAns)
        return
    subsequenceOfArr(arr,index+1,currAns)
    subsequenceOfArr(arr,index+1,currAns+[arr[index]])

def main():
    arr = [1,2,3]
    print(subsequenceOfArr(arr))
main()