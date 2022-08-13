if True:
    print('true')

else:
    print('false')


##for loops 
my_bestfriends=['shiva','vara','kaushik','vissa']


for name in my_bestfriends:
    print(name)

my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in my_list:
    if(i%2==0):
        print(f'even number is {i}')
        #or
        print('even number:{}'.format(i))
    else:
        #or 
        print('oddd number :{}'.format(i))
        print(f'odd number :{i}')
           
sum=0
for i in my_list:
    sum=sum+i

print(sum)
str='adithya hello ur welocme!'
for _ in str:
    print(_)
    print(_.upper())
    print(_.rstrip())
t=(1,2,3,4,43)
for j in t:
    print(j) 
##calling tuples in a a list by using for loops
list=[(1,2),(3,4),(5,6),(7,8)]
for i in list:
    print(i)
##tuple unpacking calling elements in tuple present ina list via method called tuple unpacking
for a,b in list:
    print('the elements in tuple in the list are {} {}'.format(a,b))
    ###or 
    print(a)
    print(b)

 ##calling dictionaries through for loops
dict={'k1':1,'k2':3444,'k3':786,'k4':12}
for _ in dict:
    print(_)
    ##here it shows only key values
for items in dict.items():
    print(items) 
for a,b in dict.items():##unpackingof dict in list by for loops
    print('{} is key and {}  is value'.format(a,b))   
    #for priting only values
    print('value is {}'.format(b)) 
##other way to unpacking dictionaries in list and their values
m_list=[]
for val in dict.values():
    print(val)
    m_list.append(val)
m_list.sort()
print(m_list)
 #list cannot be sorted if there are both strings and numbers placed together
#while loops
x=0
while x<5:
    print('x is{}'.format(x))   
    x+=1
##staetements in python 
# pass
# break
# continue
#***pass
for i in my_list:
    #comment
    pass 
print('pass tells do nothing at all')   
##***range function
new_list=list(range(1,20))
##range(start,stop,step)


