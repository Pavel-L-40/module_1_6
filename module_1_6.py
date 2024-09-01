# словари и множества

my_dict = {'Albert Einstein' : 1879, 'Nikola Tesla' : 1856, ' Isaac Newton': 1642} # создаем словарь
print((my_dict))

print(my_dict.get('Albert Einstein'))
print(my_dict['Nikola Tesla'])

print(my_dict.get('Galileo Galilei')) # при отсутствующем ключе выводит None
print(my_dict.get('Galileo Galilei', 'The key was not found')) # при отсутствующем ключе выводит второе значение метода get

my_dict.update({'Alessandro Volta' : 1745,
                'Heinrich Hertz' : 1857})
print(my_dict)

remove_contact = my_dict.pop('Heinrich Hertz')
print(remove_contact)
print(my_dict)

my_set = {1, 2, 3, 2, 3, 4, 3, 4, 5, 'string'} # создаем множество
print(my_set)

my_set.add(6)
my_set.add(66)
print(my_set)

