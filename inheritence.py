###inheretince classe in class
class Animal():
    def __init__(self):
        print('got animal')
    def it_is(self):
         print('yeah this is animal')
    def who_am_i(self):
        print('you are a human')

class Dog(Animal):  
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')   

    ###overwritting the function in base class
    def it_is(self):
        print('its changed')  
        
            
my_animal=Animal()
my_animal=Dog() 
my_animal.it_is()       

class A():#A is super class
    def feature1(self):
        print('feature 1 is working')
    def feature2(self):
        print('feature 2 is working')
class B(A):###b is child class of A or sub class of A it inheriting all features of A class
    def feature3(self):
        print('feature 3 is working')
    def feature4(self):
        print('feature 4 is working')
class C(B):
    def feature5(self):
        print('feature 5 is working')        
a1=A()
a1.feature1()
a1.feature2()
b1=B()
b1.feature1()
