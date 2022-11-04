def minimumWeight(weight,limit) :
    minimum = int(10e09)
    
    if limit == 1 :
        return sum(weight)

    for num in range(len(weight)) :
        if len(weight[num:]) < limit - 1 :
            break

        box1 = sum(weight[:num])
        box2 = minimumWeight(weight[num:],limit-1)
        minimum = min(max(box1,box2),minimum)

    return minimum

weight , limit = input("Enter Input : ").split("/")
weight = [ int(w) for w in weight.split() ]
limit = int(limit)

print("Minimum weigth for",limit,"box(es) =",minimumWeight(weight,limit))