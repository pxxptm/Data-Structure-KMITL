def getMaxIndex(list,index = 0,max = None,maxIndex = 0) :
    if index == len(list) :
        return maxIndex
    if max == None or list[index] > max :
        max = list[index]
        maxIndex = index
    return getMaxIndex(list,index + 1,max,maxIndex)
    
def straightSelectionSort(list = [],now=None) :
    if now == None :
        now = len(list) - 1
    if now < 0 :
        print(list)
        return list

    maxIndex = getMaxIndex(list[:now+1])

    if maxIndex != now :
        list[maxIndex] , list[now] = list[now] , list[maxIndex]
        print("swap",list[maxIndex],"<->",list[now],":",list)
        
    straightSelectionSort(list,now - 1)

input = list(map(int,input("Enter Input : ").split()))
straightSelectionSort(input)
