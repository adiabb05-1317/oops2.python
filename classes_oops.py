##object oriented programming
list=[1,2,3]
my_list=set(list)
print(type(list))

# class Sample():
#     pass
# my=Sample()
# print(my)
#__init__ method


class Dog():
        species='mammal'
        def __init__(self,breed,name,age):
        ###breed is an  atribute 
        #we take in the argument
            ##asigning it to self>attribute
            self.breed=breed
            self.name=name
            self.age=age
     
# my_dog=Dog(breed='huskie')##when calling class it  calls the init__function automatically
# ##here my dog is the object of class Dog
# # my_age=Dog(age=24)
# dog_name=Dog(name='huddie')
# print(my_dog.breed)
# print(dog_name.name)
# print(my_age.age)
my_dog=Dog(breed='huskie',name='julie',age=2)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.age)
print(my_dog.species)













