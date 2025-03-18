import pickle

d = dict(name='Bob', age=20, score=88)
f = open('test.txt', 'wb')
pickle.dump(d, f)
f.close()


f = open('test.txt', 'rb')
b = pickle.load(f)
f.close()
print(b)
print(type(b))
