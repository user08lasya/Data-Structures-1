my_dict = {}
my_dict = {1:'Apple' ,2: 'Ball'}
my_dict = {'name' : 'Tara',1: [2,4,3]}
my_dict = {'name' : 'Jack' , 'age' : 24}

print(my_dict['name'])
print(my_dict.get('age'))

my_dict['age'] = 27
print(my_dict)

my_dict.pop('age')
print(my_dict)

print("Address :", my_dict.get('address'))

my_dict.clear()
print(my_dict)