def FGV(numList,x,index=0) :
    if x > numList[-1] :
        return "No First Greater Value"
    if numList[index] > x :
        return numList[index]
    return FGV(numList,x,index + 1)

numList , goalList = input("Enter Input : ").split("/")
numList , goalList = sorted(list(map(int, numList.split()))), list(map(int, goalList.split()))

for num in goalList :
    print(FGV(numList,num))
