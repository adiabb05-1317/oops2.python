class student():
    def __init__(self):
        print('i am init in CLASS STUDENT')
    def _method(self):
        print(' i am method in student class')
class marks(student):
    def __init__(self):
        super()._method()
        print(' i am init class in marks class sub claas of super class student')
    def method(self):
        print('i am method in sub class')    

ob=marks()