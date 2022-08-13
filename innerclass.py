class student():
    def __init__(self,name,rollno):
        self.rollno=rollno
        self.name=name
        self.lap=self.laptop()

    def show(self):
        print(self.name,self.rollno)
       


    class laptop():
        def __init__(self):
            self.brand='hp'
            self.cpu='i5'
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)


s1=student('adithya',17)
s2=student('bhannu',27)
s1.show()
##creating object for inner class
# s1.lap.brand
# ##
# lap1=s1.lap
# lap2=s2.lap
lap1=student.laptop()
lap1.show()



