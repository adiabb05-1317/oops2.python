#using maps and filters 
def cube(num):
    return num**3


list=[1,2,3,4,5,6]
for x in map(cube,list):
    print(x)


def palindrome(str):
    new_str=str[::-1]
    if str==new_str:
        print('its palindrome')
    else:
        print('its not palindrome')

palindrome('madam')

def mul(list):
    m=1
    for i in list:
        m= m*i
    return m
n=mul([1,2,3,4])
print(n)        

def repeat(list):
    n=set(list)
    new_list=[_ for _ in n]
    return new_list
m=repeat([1,2,1,1,2,3,3,4,4,4,5,6])
print(m)

def small(list):
    c=0
    count=[]
    for i in range(len(list)):
    
         for j in range(i,len(list)):

            if list[j]<list[i]:
                c=c+1

         count.append(c)
         c=0
    return count    
l=small([5,2,6,1])
print(l)

def repeatedCharacter( s) :
        for i in range(0,len(s)-1):
            if s[i]==s[i+1]:
                k=i 
                break
                
                  
        return s[k]        
            
print(repeatedCharacter('abcdd'))





         
                   
                   