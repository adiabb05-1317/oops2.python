class computer():

    def __init__(self,cpu,ram):
       self.cpu=cpu
       self.ram=ram

    def config(self):
        print("the config is",self.cpu,self.ram)



com1=computer('i5',16)
com1.config()

    ####or we can call as 
    #computer.config(com1)

class name():
    def __init__(self):
        self.name='adithya'
        self.age='17'

    def update(self):
        self.age=31 
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

ob1=name()
ob2=name()
ob2.name='beenu'
ob2.update()
ob2.age='17'
print(ob1.name)
print(ob1.age)  
print(ob2.name)  
print(ob2.age)  
if ob1.compare(ob2):
    print('they are same')


