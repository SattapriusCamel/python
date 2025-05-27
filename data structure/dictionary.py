my_dict = {'Elvis': 'it is rick and morty time', 'type':'sandwich'}
my_dict = {1:'192', 2:'193'}
my_dict = {'Name':'Chelu', 'age':10}

print(my_dict['Name'])
print(my_dict.get('age'))

my_dict['age']=12
print(my_dict)

my_dict['friend'] = 'Chelu squared'
print(my_dict)

print("Friend: ", my_dict.get('friend'))

my_dict.clear()
print(my_dict)
