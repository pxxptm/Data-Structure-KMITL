def getPosToInsert(list,value,index=0) :
    if index == len(list) or list[index] > value :
        return index
    return getPosToInsert(list,value,index + 1)

def insertionSort(list,ans=[],index=0) :
    if index == 0 :
        ans.append(list.pop(0))
        return insertionSort(list,ans,1)
    
    if len(list) == 0 :
        print("sorted")
        print(ans)
        return
    
    value = list.pop(0)
    pos = getPosToInsert(ans,value)
    ans.insert(pos,value)
    print("insert",value,"at index",pos,":",ans,end=" ")
    if len(list) != 0 :
        print(list)
    else :
        print()

    return insertionSort(list,ans,index + 1)

input = list(map(int,input("Enter Input : ").split()))
insertionSort(input)