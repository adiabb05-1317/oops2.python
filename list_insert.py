# l=[1,2,3,4,5]
# k=len(l)+1
# new=[]
# a=int(input('enter the index of insertion:'))
# b=int(input('enter the value of insertion:'))
# if a<0:
#     a=len(l)+a+1
# else:
#     a=a-1

# l=l[:a]+[b]+l[a:len(l)]
# print(l)  


# n=[1,2,3,4,5]
# a=int(input('enter the index of insertion:'))
# b=int(input('enter the value of insertion:'))
# a-=1
# k=len(n)
# n.append(None)
# for i in range(k-1,a-1,-1):
#     n[i+1]=n[i]

# n[a]=b    
# print(n)

x=[]
n=int(input('no of elemnts in alist'))
for i in range(n):
    num=int(input())
    x.append(num)
print(x)    
a=int(input('value of insertion'))
b=int(input('index of insertion'))
k=len(x)
x.append(None)

for i in range(k-1,b,-1):
    x[i+1]=x[i]

x[b]=a
print(x)