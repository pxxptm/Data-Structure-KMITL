print("*** Mod Position ***")

strInput , modulo = input("Enter Input : ").split(",")

modulo = int(modulo)

ans = []

for i in range(len(strInput)) :
    if (i%modulo) == (modulo-1) :
        ans.append(strInput[i])

print(ans)