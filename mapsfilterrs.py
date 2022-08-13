   ### using maps
def square (num):
      return num**2 

nums=[1,2,3,4,5]  
l=list(map(square,nums))
print(l) 
#either we can print list or can call the map in looop
#      
for i in map(square,nums):
    print(i)

def slicer(str):
    if len(str)%2==0:
        return 'even'    
    else:
        return str[0]    
string=['john','adi','shiva','good','vara','kaushik']
s=list(map(slicer,string))
print(s)        

#we use filter function to get true values in function

def check_even(num):
    return num%2==0

n=[1,2,3,4,4,5,6,7,8,9,10,12]
a=list(filter(check_even,n))
print(a)
for _ in filter(check_even,n):
    print(_)

## changing function into lambda expressio 
def square(num):
    return num**2
##changing above function into a lambda expression 
square=lambda num:num**2  ##like function   
print(square(2))
##using maps with lambda expression
n=[1,2,3,4,4,5,6,7,8,9,10,12]
new=list(map(lambda num:num%2,n))
print(new)
##using filter with lambda expression
g=list(filter(lambda num:num%2==0,n))
print(g)
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))