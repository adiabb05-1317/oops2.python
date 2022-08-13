class cordinates():
    def __init__(self,a,b):
        self.x1=a[0]
        self.y1=a[1]
        self.x2=b[0]
        self.y2=b[1]
        print(self.y2)
    def slope(self):
        return (self.y2-self.y1)/(self.x2-self.x1)  
    def distance(self):
       return ((self.x2-self.x1)**2 - (self.y2-self.y1)**2)**0.5
       
c1=cordinates((3,2),(8,12))  
c1.slope()
c1.distance() 
print(c1.slope()) 
print(c1.distance())

class line():
    def __init__(self,c1,c2):
        self.c1=c1
        self.c2=c2
    def slope(self):
        x1,y1=self.c1
        x2,y2=self.c2
        return( y2-y1)/(x2-x1)    

    def distance(self):
        x1,y1=self.c1
        x2,y2=self.c2
        return ((x2-x1)**2 -(y2-y1)**2 )**0.5
c1=line((3,2),(8,12))
print(c1.slope())
print(c1.distance())