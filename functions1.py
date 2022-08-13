from re import I


def myfunc(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            return a

        else:
            return b
    elif a%2!=0 and b%2!=0:
        if a>b:
            return a
        else:
            return b           

n=myfunc(2,4)             
print(n)

def func(name):
    fname=name[:3]
    lname=name[3:]
    return fname.title()+lname.title()


n=func('adithya')    
print(n)

def str_fun(str):
    list=str.split()
    print(list)
    list.reverse()
   
    return ' '.join(list)

s=str_fun('i am ready')
print(s)

def round(num):
    if num+10==100 or num-10==100:
        return True
    elif  num+10==200 or num-10==200: 
        return True 
    else :
        return False
n=round(90)
m=round(240)
print(n)   
print(m)

def list(list):
    for i in list:
        if list[i]==3 and list[i+1]==3 :
            return True
        else :
           return False

print(list([1,2,3,4,5,3,3,6]))                
def str(string):
    list=[]
    for _ in range(len(string)):
        list.append(3*string[_])
    return ''.join(list)    


g=str('hello')
print(g)
#Given three integers between 1 and 11, if their sum is less than or equal to 21, 
# return their sum. If their sum exceeds 21 and there's an eleven, reduce 
# the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def add(a,b,c):
    s=sum((a,b,c))
  
    if s<=21:
        return s
    elif  s>21:
        if a ==11 or b==11 or c==11:
            return s-10
    elif s>21:
        return 'BUST'           

s=add(24,2,11)
print(s)

 


def m_69(list):
    s=0
    add= True
    n=range(len(list))
    print(n)
    for i in range(len(list)):
        if list[i]!=6 :
            s=s+list[i]

        else:
            while list[i]!=9:
                 list[i]=0
                 i+=1
            list[i]=0     
    print(list)
    return s         

n=m_69([2,1,6,7,9,11])
print(n)


def order(list):
  for i in range(len(list)):
    if list[i]==0:
        if list[i+1]==0 and list[i+2]==7:
            return True
    else :
        return False
ord=order([12,2,3,0,3,0,7,8])
print(ord)

def check(list):
    code=[0,0,7,'x']
    for i in list:
        if i==code[0]:
            code.pop(0)

    if len(code)==1:
        return True
n=check([1,2,3,0,0,7,5])
print(n)

def string(str):
    list=[]
    for i in str:
           for j in range(97,123):
               if i==chr(j):
                     list.append(j)
    new_list=[x for x in range(97,123)]
    list.reverse()
    if set(new_list)==set(list)  :
        return True
    else :
        return False
n=string("The quick brown fox jumps over the lazy dog")            
print(n)



















        


