price = [10, 20, 30, 40, 50]
# 1. 将价格列表按升序排序。
price.sort()
print(price)
# 将价格列表反转，以得到降序排序的列表。
price_reversed = price[::-1]  # 使用切片反转列表，得到降序排序
print("降序排序后的价格列表:", price_reversed)

# 找到最高价格和最低价格。
max_price = max(price)  # 获取最高价格
min_price = min(price)  # 获取最低价格
print("最高价格:", max_price)
print("最低价格:", min_price)

# 计算所有商品的平均价格。
average_price = sum(price) / len(price)  # 计算平均价格（总和除以数量）
print("平均价格:", average_price)

"""
请编写一个程序，实现以下功能：

1. 定义一个列表 my_list，包含至少五个元素，例如 [1, 2, 3, 4, 5]。
2. 将列表 my_list 中的元素进行相加，并将结果输出。
3. 将列表 my_list 中的元素重复两次，并将结果输出。
4. 判断数字 3 是否在列表 my_list 中，并输出判断结果。
5. 使用 max() 函数找出列表中的最大值，并输出。
6. 使用 min() 函数找出列表中的最小值，并输出。
"""
my_list = [1, 2, 3, 4, 5]
sum_result = sum(my_list)
print("列表元素相加的结果:", sum_result)
doubled_list = my_list * 2
print("列表元素重复两次的结果:", doubled_list)
is_3_in = 3 in my_list
print("数字3是否在列表中:", is_3_in)
max_value = max(my_list)
print("列表中的最大值:", max_value)
min_value = min(my_list)
print("列表中的最小值:", min_value)



# 请编写一个程序，使用 while...else... 循环语句，从 1 到 10 的数字中，输出所有奇数，并在循环结束后输出 "已完成"

num = 1
while num <= 10:
    if num % 2 != 0:
        print(num)
    num += 1            
print("已完成")

# 编写一个程序，找出从 1 到 100 的所有整数中能被 7 整除但不能被 5 整除的数字，并计算它们的总和
sum = 0
for i in range(1, 101):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
        sum += i
print("总和为:", sum)
"""
假设你正在开发一个在线商店的购物车功能，需要编写 Python 代码来处理购物车内的商品。请完成以下要求：


已知有一个购物车商品列表 cart = [("Apple", 2), ("Banana", 3), ("Orange", 4), ("Pear", 1)]，
其中每个元组表示一种商品及其数量。请使用列表推导式编写代码，实现以下功能：

1. 创建一个新列表 cart_items，其中仅包含购物车中的商品名称（即去除商品数量信息）。
2. 创建一个新列表 expensive_items，其中仅包含购物车商品数量>=3的商品名称。
3. 将购物车中每个商品的数量加倍，并创建一个新的购物车列表 cart_doubled。
4. 请编写上述要求的代码，并输出最终的列表 cart_items、expensive_items 和 cart_doubled。
"""
cart = [("Apple", 2), ("Banana", 3), ("Orange", 4), ("Pear", 1)]
cart_items = [item[0] for item in cart]
print("购物车中的商品名称:", cart_items)
expensive_items = [item[0] for item in cart if item[1] >= 3]
print("购物车中商品数量>=3的商品名称:", expensive_items)
cart_doubled = [(item[0], item[1] * 2) for item in cart]
print("购物车中每个商品的数量加倍:", cart_doubled)

print("cart_items:", cart_items)
print("expensive_items:", expensive_items)  
print("cart_doubled:", cart_doubled)

"""
统计字符串中，各个字符的个数，"hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1，使用程序实现。
"""
str = "hello world"
char_count = {}
for char in str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)