class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:

    def __init__(self,items,tableSize,maxCollision) :
        self.items = items
        self.tableSize = tableSize
        self.maxCollision = maxCollision

    def isFull(self) :
        for item in self.items :
            if item == None :
                return False
        return True

    def ASCII(self,key) :
        ascii = 0
        for ch in key :
            ascii += int(ord(ch))
        return ascii

    def index(self,keyASCII) :
        return keyASCII % self.tableSize

    def QuadraticProbing(self,keyASCII) :
        collision = 1
        index = self.index(keyASCII)
        while self.items[index] != None :
            print("collision number",collision,"at",index)
            if collision >= self.maxCollision :
                print("Max of collisionChain")
                return
            index = ( keyASCII + pow(collision,2) ) % self.tableSize
            collision += 1
        return index

    def printTable(self) :
        for i in range(len(self.items)) :
            print("#",i+1,"	",self.items[i],sep="")
        print("---------------------------")

print(" ***** Fun with hashing *****")

condition,data = input("Enter Input : ").split("/")
tableSize , maxCollision = map(int,condition.split())
data = [ item for item in data.split(",") ]

TABLE = [ None ] * tableSize
HASHTABLE = hash(TABLE,tableSize,maxCollision)

for item in data :
    if HASHTABLE.isFull() :
        print("This table is full !!!!!!")
        break
    key , value = item.split()

    index = HASHTABLE.QuadraticProbing(HASHTABLE.ASCII(key))

    if index != None :
        TABLE[index] = Data(key,value)

    HASHTABLE.printTable()