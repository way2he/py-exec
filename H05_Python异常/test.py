"""
将用户输入的姓名、年龄、性别写入output.txt文件（覆盖或新建），并输出完成提示。
"""

# 获取用户输入
name = input("请输入您的姓名：")
age = input("请输入您的年龄：")  
gender = input("请输入您的性别：")

content = f"姓名：{name}\n年龄：{age}\n性别：{gender}"

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(content)  

print("写入完成！")