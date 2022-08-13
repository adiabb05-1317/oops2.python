class A():##super class
    def __init__(self):
        print('init in A')
    def feature1(self):
        print('i am a feature of A')
class B(A):##sub class
    def __init__(self):
         super().__init__()#it calls init of super class
         print('init in B')
    def feature1(self):
        print('i am a feature of A')        
a1=B()
#at first it calls init function of A
#if there init function in B then it calls B
#if not i t calls A
#here to call init method  of A
print("!!next output")
class A():#A is super class
    def feature1(self):
        print('feature 1_A is working')
    def __init__(self):
        print('init in A')    
    def feature2(self):
        print('feature 2 is working')
class B():###b is child class of A or sub class of A it inheriting all features of A class
    def feature1(self):
        print('feature 1_B is working')
    def __init__(self):
        print('init in B')        
    def feature4(self):
        print('feature 4 is working')
class C(A,B):##c inherites both a nd b where a and b are not inherited u can see rit
    def feature5(self):
        print('feature 5 is working') 

    def __init__(self):
        super().__init__()##here A and B are two super classes but it calls only A 
        #bcz A is the first it flws order
        print('init in C')    
    def feat(self):
        super().feature2()              
a1=C()
a1.feature1()
a1.feat()



       