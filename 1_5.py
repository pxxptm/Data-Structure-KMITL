from operator import length_hint


print("*** Fun with countdown ***")
print("Enter List : " , end="")

input = input()
userInput = list(map(int, input.split()))

temp = [userInput[0]]
ans = []
final = []

i = 1

for i in range(length_hint(userInput)) :

    if userInput[i] == userInput[i-1] - 1 :

        temp.append(userInput[i])

        if userInput[i] == 1 :
            ans.append(temp)
            temp = [userInput[i]]
    else :

        if userInput[i] == 1 :
            temp.append(userInput[i])
            ans.append([1])
            temp = [userInput[i]]
        else :
            temp = [userInput[i]]

final.append(len(ans))
final.append(ans)
print(final)
