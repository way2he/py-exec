mydict = { }
mydict[1] = 1
mydict['1'] = 2
mydict[1.0] = 3
print(mydict)
print(mydict[1] + mydict['1'] + mydict[1.0])