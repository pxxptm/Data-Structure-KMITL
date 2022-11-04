
class Calculator :

    def __init__(self,value) :
        self.value = value

    def __add__(self,another) :
        return self.value + another.value

    def __sub__(self,another) :
        return self.value - another.value

    def __mul__(self,another) :
        return self.value * another.value
        
    def __truediv__(self,another) :
        return self.value / another.value

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")