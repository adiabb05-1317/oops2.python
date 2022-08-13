print("the string")
a=len('the string')
print(a)
#indexing
mystring="adithya"
c=mystring[0:3]
print(c)
print(mystring[-3])
str="abcdefgh"
#slicing
n=str[1:]
n=str[2:]
n=str[:5]
n=str[3:6]
print(n)
#step size
#inc or dec in string slicing by steps && string slicing has [start:stop:step/path]
n=str[::3]
g=str[2::1]
print(n)
print(g)
str1="abcdefghijk"
new=str1[::-1]
print(new)
#string concatination
new="all"+str1
new='all'+str1
print(new)
x="awesome"
print(x+" it is beautiful outside")
x=x+" it is beautiful outside"
#we can get repeating strings by multiplication
y=x*10
print(y)
a='ahir'
print(a*5)
k='2'+'56'
print(k)
str3="adithya"
#string built in functions 
print(str3.rfind("h"))#finding letter or char in string
print(str3.upper())#for changing string to upper case
print(str3.lower())#for changing string to lower case



##for splitting string into a list we use split example below
#here below it splits on basis of white space
str3="adithya beenu bhannu  ahir "
list=str3.split()
print(list)
#here we see how it splits by parameter
list1=str3.split('i')
print(list1)
name="adithya"
print('hello!! '+name+' sir')
##formatting string *******
print("hi this is {}".format('adithya'))
print("hi this is {} {} {}".format('adithya','beenu','bhannu'))
num=(56+76)**2
print('the output is {}'.format(num))
print('order is {} {} {}'.format('in ','5min','comming'))
print('order is {2} {0} {1}'.format('in ','5min','comming'))
print('we are {a} {b} {c}'.format(a='adi',b='beenu',c='bhannu'))
###formatting with floating values/float
#***syntax {value:width.precision f}
result=1234/44
print('the result is {r:1.4f}'.format(r=result))#this middle parameter width gives 50 spaces
#other method to fromat string is below
order='adithya'
print(f'the order is coming and its {order} order')
print(f'the result is {result}')   
print('the answer is {:.2f}'.format(result)) 
f_name='adithya'
m_name='kanneti'
print(f'{f_name} {m_name}{name}')
##capitalze
str='adithya'
print(str.capitalize())
print()