def myfunc(*args):
    return sum(args)*0.05
    
n=myfunc(100,40,60)
print(n)

def my_func(a,b):
    return sum((a,b))*0.05

print(my_func(100,40))  

#**kargs
#kargs arguments are dictionaries
def my_func(**kargs):
    print(kargs)
    if 'fruit' in kargs:
        print('the fruit is {}'.format(kargs['fruit']))
    else:
        print('i did not find any fruit here') 
   

my_func(fruit='apple',key=200,veggie='cabbage')

##using both args and kargs
def function(*args,**kargs):
    print(args)
    print(kargs)
    print('i like {} {}'.format(args[0],kargs['food']))

function(10,20,30,fruit='apple',key1=23,key3=78,food='biriyani')


def new_fun(*args):
    list=[]
    for i in args:
        if i%2==0:
            list.append(i)
    return list
g=new_fun(1,2,3,4,5,6,7,89,9,10)
print(g)


def myfunct(str):
    string=[]

    for i in range(len(str)):
        if i%2==0:
            string.append(str[i].upper())
        else:
            string.append(str[i].lower())
        
    return ''.join(string)
n_string=myfunct('adithyaisgoodhandsome')
print(n_string)




    
    