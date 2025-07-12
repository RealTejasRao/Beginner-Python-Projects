class vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def __add__(self, q):
        return vector(self.a+q.a, self.b+q.b)
    
    def __sub__(self,q):
        return vector(self.a-q.a, self.b-q.b)
    
    def __mul__(self,q):
        return vector(self.a*q.a, self.b*q.b)
    
    def __truediv__(self,q):
        return vector(self.a/q.a, self.b/q.b)
    
    def mag(self):
        return ((self.a)**2+(self.b)**2)**0.5
    
    def __repr__(self):
        return f"The coordinates are ({self.a}, {self.b})"
    

p1= vector(1,2)
p2= vector(3,4)
p3= p1+p2
p4= p1-p2
p5= p1*p2
p6= p1/p2

print(p3.mag())

print(repr(p3))
print(repr(p4))
print(repr(p5))
print(repr(p6))
