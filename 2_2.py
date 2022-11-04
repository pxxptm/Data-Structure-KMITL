people = 0
fare = 0

class Bus:

    def __init__(rhs,people,fare):
        rhs.people = people
        rhs.fare = fare

    def __str__(rhs):
        return 'this bus has ' + str(rhs.people) + ' people with fare = ' + str(rhs.fare)

    def __lt__(rhs1,rhs2):
        return rhs1.people*rhs1.fare < rhs2.people*rhs2.people

    def people_in(rhs,k):
        rhs.people += k
        return rhs.people

    def people_out(rhs,k):
        rhs.people -= k

        if rhs.people < 0 :
            rhs.people = 0
             
        return rhs.people

    def change_fare(rhs,new_fare):
        rhs.fare = new_fare
        return rhs.fare

b1, b2, f1, f2 = input("Enter people in Bus1, Bus2, fare Bus1, Bus2 : ").split()

b1 = Bus(int(b1), int(f1))
b2 = Bus(int(b2), int(f2))

if b1 < b2 :
    print(b1)
else:
    print(b2)

b1.people_in(3)
b1.people_out(6)
b1.change_fare(12)
print(b1)