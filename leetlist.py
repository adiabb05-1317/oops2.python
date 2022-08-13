def merge(list1,list2):
    new_list=list1+list2
    new_list.sort()
    return new_list
a=merge([],[0])    
print(a)


def list(l):
    k=len(l)
    n=set(l)
    new_list=[x for x in n]
    g=len(new_list)
    for i in range(g,k):
        new_list.append('_')
    return g,new_list
print(list([0,1,1,2,3,4,5,4,3,4,2,3,4,1,2,3,4,78,9,40,35,26]))

a=int(input())
for i in range(a):
      b,c=input( ).split()
      print(int(b)*4+int(c) )
     
