from stat import SF_ARCHIVED


class marks():
    topper='100'
    def __init__(self,adi,shiva,vara):
        self.adi=adi
        self.shiva=shiva
        self.vara=vara

        ###operations methods used in classes
    def name(self,num):
        print('Topper!! {} scored out of {} marks!'.format(self.adi,num))
all_marks=marks(95,28,33)   
print(all_marks.adi)
print(all_marks.shiva)  
all_marks.name(100)


