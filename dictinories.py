#dictionaries has curly braces 
my_dict={'key1':'adithya','key2':'beenu','key3':'bhannu','key4':'ahir'}
print(my_dict['key2'])
print(my_dict['key3'])
prices={'apples':100,'grapes':500,'banana':40}
print(prices['apples'])
##we can have dictionaries inside the dictionaries can create list with in the dictionery 
d={'1':123,'2':[3,4,5,6],'3':{'k1':200,'k2':'tomatoes','k3':'bananas'}}
##calling dictinonaries inside dictionaries
print(d['3']['k2'])
##calling list element in the dictionary by keyword and thenn indeexing 
print(d['2'][2])
my_dict={'k1':['a','b','c','d']}
letter=my_dict['k1'][2]
cap_letter=letter.upper()
print(cap_letter)
#or directly we can make it to uper case
print(my_dict['k1'][3].upper())#here it calls key and then index of list in that key called
print(my_dict['k1'][1:3])
##changing the values in dictionary
new_dict={'k1':200,'k2':4000,'k3':'good'}
new_dict['k2']='NEW VALUE'
print(new_dict)
##for callin or printing the key values of dictionaries 
print(new_dict.keys())
##for calling values of keys in dict
print(new_dict.values())
#calling items in dictionaries:pairs of keys and thier respective values 
print(new_dict.items())