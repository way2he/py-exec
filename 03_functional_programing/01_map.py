# map
def f(x):
    return x * x


print(list(map(f, range(1, 11))))

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def normalize(name):
    return name.upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)