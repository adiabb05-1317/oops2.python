#function for cecking even number
from re import A


def even_num(num):
    if num%2==0:
        print('{} is even number'.format(num))
    else:
        print('{} is odd number'.format(num))    
even_num(9)   



def even_check(list):
    for i in list:
        if i%2==0:
            print('{} its even number'.format(i))

        else:
            print(f' {i}its an odd number')    

numlist=[1,2,3,4,5,6,7,8,33,45,67,34,46]
even_check(numlist)
##TUPPLE UNPAKING WITH FUNCTIONS
lest=[(1,2),(3,4),(32,34)]
def myfun(lest):
    for a,b in lest:
       print(f'{a} and {b}')
lest=[(1,2),(3,4),(32,34)]
myfun(lest)
##employee worked more hours

def work(list):
    max=0
    for x ,y in list:
        
        if y>max:
            max=y
            emp=x
            
        else:
            pass    
    return emp
    

work_hours=[('abb',300),('any',4000),('andy',800),('adi',7677)]
emp=work(work_hours)
print('{} is the best employee worked for more hours'.format(emp))
def player_guess():
    guess=''
    while guess not in [1,2,3]:
        guess=int(input('enter the number 1,2 or 3'))
    return guess    

a=player_guess()
print(f'{a} is the guess')


