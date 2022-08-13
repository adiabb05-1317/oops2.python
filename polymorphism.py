from re import M


class dog():
    def __init__(self,name):
        self.name=name
    def barks(self):
        return self.name+" bowww!!"   
class cat():
    def __init__(self,name):
        self.name=name
    def barks(self):
        return self.name+" meoww!!"        

a=dog('shuffer')
b=cat('spunky')
print(a.barks())
print(b.barks())
for pet in [a,b]:
    print(type(pet))
    print(type(pet.barks()))
def pet_speaks(pet):
    print(pet.barks())    

pet_speaks(a)  
pet_speaks(b)     

class Animal():##abstract method
    def __init__(self,name):
        self.name=name
    def speak(self):
        raise NotImplementedError('subclass must implement this abstract method')    
       
my_animal=Animal('fred')       

