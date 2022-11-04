def isPrime(number) :
    if number == 2 or number == 3 :
        return True

    if number % 2 == 0 or number == 1 :
        return False

    for i in range(3,int(pow(number,1/2))+1) :
        if number % i == 0 :
            return False

    return True

class hash:

    def __init__(self,tableSize,maxCollision,threshold) :
        self.items = [None] * tableSize
        self.original = []
        self.tableSize = tableSize
        self.maxCollision = maxCollision
        self.threshold = threshold

    def isFull(self) :
        for item in self.items :
            if item == None :
                return False
        return True
        
    def isOverThreshold(self) :
        if self.tableSize * self.threshold / 100 < self.sizeOfHash() + 1 :
            return True
        else :
            return False

    def QuadraticProbing(self,num) :
        collision = 0
        index = num % self.tableSize
        while self.items[index] != None :
            collision += 1
            print("collision number",collision,"at",index)
            if collision >= self.maxCollision :
                print("****** Max collision - Rehash !!! ******")
                self.rehash()
                self.insert(num)
                return None
            index = ( num + pow(collision,2) ) % self.tableSize
        return index

    def newSize(self) :
        new = 2 * self.tableSize + 1
        while not isPrime(new) :
            new += 2
        return new

    def sizeOfHash(self) :
        return len(self.items) - self.items.count(None)

    def insert(self,val) :
        index = self.QuadraticProbing(val)
        if self.isOverThreshold() :
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash()
            self.insert(val) 
        elif index != None :
            self.items[index] = val
            self.original.append(val)

    def rehash(self) :
        original = self.original
        size = len(self.items)
        self.items = [None] * self.newSize()
        self.tableSize = len(self.items)
        self.original = []
        for i in original:
            if i != None:
                self.insert(i)          

    def printTable(self) :
        for i in range(len(self.items)) :
            print("#",i+1,"	",self.items[i],sep="")
        print("----------------------------------------")

print(" ***** Rehashing *****")

condition,data = input("Enter Input : ").split("/")
tableSize,maxCollision,threshold = map(int,condition.split())
data = map(int,data.split())

h = hash(tableSize,maxCollision,threshold)

print("Initial Table :")

h.printTable()

for i in data :
    print("Add :",i)
    h.insert(i)
    h.printTable()