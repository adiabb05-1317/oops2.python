
st='print only words that start with s statement'
list=st.split()
print(list)    
for word in list:
    if word[0]=='s'or 'S':
        print(word)
#other
for _ in range(0,10):
    if _%2==0:
        print(_)
#other 3
new_list=[num for num in range(0,50) if num%3==0]
print(new_list)      
#other 4
str = 'Print every word in this sentence that has an even number of letters'
str_list=str.split()
for i in str_list:
    if len(i)%2==0:
        print(i)
#other 4
for num in range(1,100):  
    if num%5==0 and num%2==0:
        print("FizzBuzz")
    elif num%5==0:
        print("Buzz")  
    elif num%3==0:
        print('Fuzz')
    else :
        print(num) 
st = 'Create a list of the first letters of every word in this string'
s_list=st.split()
for w in s_list:
    print(w[0])




