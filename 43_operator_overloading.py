
class Point :
    
    def __init__(self,x,y):
        self.x=x;
        self.y=y;
    
    def initial_point(self):
        print (f"initial point are  {self.x} and {self.y}")    
    def sum_point(self,p):
        return Point((self.x + p.x),(self.y + p.y))
    
    def print_point(self):
        print(f"points are {self.x} and {self.y}")
        
    def __add__(self, p):
        return Point((self.x + p.x),(self.y + p.y))
    
    def __sub__(self, p):
        return Point((self.x - p.x),(self.y - p.y))
    
    def __mul__(self, p):
        return Point((self.x * p.x),(self.y * p.y))
    
    def __truediv__(self, p):
        return Point((self.x / p.x),(self.y / p.y))
        
p1=Point(20,40)
p2=Point(5,4)
p1.initial_point()
p2.initial_point()
# p=p1.sum_point(p2)  # it return a new point which is sum of p1 and p2
# OR we can directly overload the operator by built-in method provided by python 
print("After Operator overLoading ...\n")
p=p1+p2; #we overloaded the + operator by writng __add __ function .
p.print_point()

p=p1-p2; #we overloaded the - operator by writng __sub __ function .
p.print_point()

p=p1*p2; #we overloaded the * operator by writng __mul __ function .
p.print_point()

p=p1/p2; #we overloaded the / operator by writng __truediv __ function .
p.print_point()


