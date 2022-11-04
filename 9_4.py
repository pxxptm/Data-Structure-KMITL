l = [e for e in input("Enter Input : ").split()]

if l[0] == 'EX':
    Ans = "merge sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : " + Ans)
else:

    def sortInsert(list,value,index=0) :
        if index == len(list) or list[index] > value :
            list.insert(index,value)
            return list
        return sortInsert(list,value,index + 1)

    l = list(map(int, l))
    sortedList = [l[0]]

    for i in range(len(l)) :
        if i%2 == 0 :
            med = sortedList[int(len(sortedList)/2)]
        else :
            med = ( sortedList[int(len(sortedList)/2)-1] + sortedList[int(len(sortedList)/2)] ) / 2

        print("list =",l[:i+1],": median = {:.1f}".format(med))

        if i < len(l) - 1 :
            sortInsert(sortedList,l[i+1])
