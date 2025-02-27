# -*- coding: utf-8 -*-
print('abC'.encode('ascii'))

# 要计算str包含多少个字符，可以用len()函数：
print(len('Abc'))
print(len('中文'))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(b'ABC')
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
per = ((85 - 72) / 72) * 100
print(f'小明的成绩提升了 {per:.1f}%')
print('小明的成绩提升了 %.1f%%' % per)
