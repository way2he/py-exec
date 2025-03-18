# try:
#     f = open('/Users/heshiyuan/Desktop/aaa.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
#
# with open('/Users/heshiyuan/Desktop/aaa.txt', 'r') as f:
#     print(f.read())


with open('/Users/heshiyuan/Desktop/aaa.txt', 'r', encoding='utf8') as f:
    print(f.readline())
    for line in f.readlines():
        print(line)


with open('/Users/heshiyuan/Desktop/aaa.txt', 'w', encoding='utf8') as f:
    f.write('hello world')
    f.close()

# 覆盖写入
with open('/Users/heshiyuan/Desktop/aaa.txt', 'a', encoding='utf8') as f:
    for i in range(10):
        f.write('hello world111111\n')
    f.close()

