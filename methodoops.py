class student():
    clg='ngit'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3 

    def get_m1(self):
        return self.m1

    def set_m1(self,value):
        self.m1=value 

    @classmethod##it is a decorator to use a class method

    def getclg(cls):#here we use cls variable not self because clg is class object not an instance
     
             
             return cls.clg
    @staticmethod         
    def info():###this is a method where we dont use obj or class
        print('this is student class in abc module')

s1=student(13,24,23)
s2=student(24,32,34)
print(s1.avg())
print(s2.avg())
print(student.getclg())
s1.info()