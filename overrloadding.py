class student():
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2 
        s3=student(m1,m2)
        return s3

s1=student(30,45)
s2=student(45,89)                
s3=s1+s2  ##-> s3=student__add__(s1,s2)
print(s3.m2)
