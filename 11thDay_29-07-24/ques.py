def printDuplicate(arr):
    # st = []
    # dup = []
    # for i in range(len(arr)):
    #     if arr[i] in st and arr[i] not in dup:
    #         dup.append(arr[i])
    #     st.append(arr[i])
    # return dup
    for i in arr:
        wholeXor = wholeXor^e
        if wholeXor^e == 0:
            return e



def main():
    arr = [8,9,3,-1,12,16,12,9,-1]
    print(printDuplicate(arr))
main()