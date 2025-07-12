class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def mag(self):
        return ((self.a)**2+ (self.b)**2)**0.5
    
    def __gt__(self,other):
        return self.mag()>other.mag()
    
    def __lt__(self,other):
        return self.mag()<other.mag()
    
    def __ge__(self,other):
        return self.mag()>=other.mag()
    
    def __le__(self,other):
        return self.mag()<=other.mag()
    
    def __eq__(self, other):
        return self.mag()== other.mag()
    
p1= Vector(1,2)
p2= Vector(1,2)

print(p1>p2)     # False
print(p1<p2)     # True
print(p1>=p2)    # False
print(p1<=p2)    # True
print(p1==p2)    # False