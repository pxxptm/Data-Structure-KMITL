def hbd(age):

    if age%2 == 0 :
        return "saimai is just 20, in base " + str(int(age/2)) + "!"
    else :
        return "saimai is just 21, in base " + str(int(age/2)) + "!"

year = input("Enter year : ")

print(hbd(int(year)))