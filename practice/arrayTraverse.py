def sufficientFoodForRat(arr,n,r,unit):
    # r = 40
    unit = 2
    required_food = r*unit
    sumF=0
    count = 0
    if n == 0:
        return -1
    for i in range(n):
        if sumF >= required_food:
            return count
        else:
            sumF = sumF+arr[i]
            count+=1
    if required_food > sumF:
        return 0

        
def main():
    homeNumberArr = [2,8,3,5,7,4,1,2]
    lenOfHome = len(homeNumberArr)
    numOfRat = 7
    unitOfFoodToBeConsumedByRat = 2
    print(sufficientFoodForRat(homeNumberArr,lenOfHome,numOfRat,unitOfFoodToBeConsumedByRat))
main()
