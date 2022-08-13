##for splitting string into a list we use split example below
#here below it splits on basis of white space
str3="adithya beenu bhannu  ahir "
list=str3.split()
print(list)
#here we see how it splits by parameter
list1=str3.split('i')
print(list1)
my_list=[1,2,3,'adi','beenu','bhannu','all']
l=len(my_list)
print(l)
print(my_list[4])
#adding lists
new_list=[1,2,3,3,6,7,67]
list=new_list+my_list
print(list)
#***slicing in list
crct_list=my_list[:4]
crct_list =my_list[:]
crct_list=my_list[2:5]
print(crct_list)
##**changing elements in list 
cycles=['bsa','hero','mountain bike','spunk']
cycles[2]='new one'
print(cycles)
#adding elemnts to end odf list
cycles.append('ladybird')
print(cycles)
#pop method
#pop is like stack lifo last input first output pop 
print(cycles.pop())
print(cycles)
popped=cycles.pop(0)
print(popped)
#sorting **** list
new_list=['d','e','f','g','a']
num_list=[6,5,74,59,34]
new_list.sort()
num_list.sort()
print(new_list)
print(num_list)
#if we try to assign sortedd list to the list it takes none
#example below
my_list=new_list.sort()
print(my_list)
#so we should assign like below
new_list.sort()
my_list=new_list
print(my_list)
##reversing list**
my_list.reverse()
print(my_list)
##nesting list**
list1=[1,2,3]
list2=[4,5,6]
list3=[1,2,1]###***matrix has three rows and colums 0,1,2
matrix=[list1,list2,list3]
print(matrix[0])
print(matrix[1][1])#1st row and 1st column elemnt(here 0 is staring row and column so 1st is 2nd row and clumn)
g_list=[1,2,3,4,5,667,88]
g_list.insert(3,334)# .insert(before index,element inserting)
print(g_list)
list=[1,2,3,4]
num_1=sum(list)
print(num_1)
n_list=[1,2,3,4,5,6,7]
n_list.insert(5,12)##insert(index,put value)
print(n_list)

for i in range(-1,-3):
    print(i)