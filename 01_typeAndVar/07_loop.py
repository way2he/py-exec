names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 计算1-10的整数之和，可以用一个sum变量做累加：
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)


print(list(range(30)))


sum = 0
for x in range(101):
    sum = sum + x
print(sum)


sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')


n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)