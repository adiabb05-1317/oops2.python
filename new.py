def string(str):
    k=None
    for i in  range(len(str)-1):
      if str[i]==str[i+1]:
         k= str[i]
         return k
         break

    if k==None:
        for i in range(len(str)):
            for j in range(i+1,len(str)):
                if str[i]==str[j]:
                    k= str[j]
                    return k
                    break
                
str='uaeiou'
o=string(str)
print(o)

