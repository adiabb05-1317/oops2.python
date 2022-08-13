# mystring='adithya'
# mylist=[]
# for _ in mystring:
#     mylist.append(_)
# print(mylist)
#*****OTHER IMP LIST COMPREHENSATION
mystring='adithya'
mylist=[letter for letter in mystring]
print(mylist)
##**other
list=[]
tup=(1,2,3,4)
list=[_ for _ in tup]
print(list)
##other
new_list=[x for x in range(1,50,5)]
print(new_list)
##for making list of cube numbers of range(0,100)
newlist=[num**3 for num in range(1,10)]
print(newlist)
##for making a list of even number of 1 to 100 range
lis=[n for n in range(1,100) if n%2==0 and n!=0]
print(lis)
#other**
metrs=[1,2,3]
cm=[(m*100) for m in metrs]
print(cm)
new_cm=[]
##by using for loop
for meter in metrs:
    new_cm.append(meter*100)
print(new_cm)  
###other**
n=[1,2,3,4]
q=[23,34,56,7]
r=[]
for i in n:
    for j in q:
        r.append(i*j)
        
print(r)
##by list comprehncation
g=[x*y for x in n for y in q]



