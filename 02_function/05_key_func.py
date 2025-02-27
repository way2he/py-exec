# 关键字函数

def person(name, age, **kw):
    print(name, age, kw)

person("张三", 18)

person("李四", 20, city="Beijing", gender="M")