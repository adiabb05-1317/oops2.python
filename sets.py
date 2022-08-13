#sets caan intialize like below 
a=set()
#adding elements in the set
a.add(1)
a.add(2)
a.add(3)
print(a)
#set doesnt repeat same elements 
a.add(1)
a.add(2)
a.add(4)
print(a)
###****casting list to set
my_list=[1,1,1,1,1,2,2,2,23,3,3,3,3,3,12]
b=set(my_list)
print(b)
