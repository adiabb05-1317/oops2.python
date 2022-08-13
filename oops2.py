class circle():
    #class objct attribute
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
        self.area=radius**2*circle.pi
       
    ##method
    def get_circumference(self):
        return self.radius*self.pi*2

my_circle=circle(5)           
print(my_circle.pi)
print(my_circle.radius)
a=my_circle.get_circumference()
print(a)
print(my_circle.area)

