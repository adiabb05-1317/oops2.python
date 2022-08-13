##range
#range(start,stop,,step)
#ENUMERATED FUNCTION/****
a='adithya'
for letter in enumerate(a):
    print(letter)
    ##here enumrated function shows the index and letter iike tupple (index,letter) in string
#unpacking enumerated
for x,y in enumerate(a):
    print(y)
##ZIP*** function
my_list=[12,2,13,45]
new_list=['a','b','c','d']
ano_list=[2,33,44,55]
print(zip(my_list,new_list))
for i in zip(my_list,new_list):
    print(i)
    ##***HERE ZIP FORMS TUPPLE OF BOTH ELEMENTS OF SAME INDEX IN BOTH THE LISTS
for _ in zip(my_list,new_list,ano_list):
    print(_)
##for insering tupples of 3 lists in one list by zip
zip_list=list(zip(my_list,new_list,ano_list))    
print(zip_list)
##unpacking of zip list
for a,b,c in zip(my_list,new_list,ano_list):
    print(c)
print('z' in ['d','y','z'])
print(2 in [1,2,3])
b=5 in (2,3,6)
print(b)
###random  modules

from random import shuffle
g_list=[1,2,3,4,5,6,7]
shuffle(g_list)##SHUFFLE IS INPLACE FUNCTION IT CANT ASSIGNED TO VARABLE JUST IT MAKES CHANGES IN THAT LIST
print(g_list)
from random import randint
a=randint(0,100)
b=randint(2,30)
print(a)
print(b)
##input function 
x=input('enter ur name:')
y=int(input('number:'))
print(x)
print(y)