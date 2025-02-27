names = {'a' : 1, 'b' : 2}
print(names['b'])

names['c'] = 3
print(names['c'])
print(names)

names.pop('c')
print(names)
print(names.get('a'))
print(names.get('c'), -1)