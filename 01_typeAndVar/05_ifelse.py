age = input('请输入您的年龄：')
age = int(age)
if age < 15:
    print("你是少年")
elif age < 30:
    print("你是青年")
elif age < 45:
    print("你是壮年")
elif age < 60:
    print("你是中老年")
else:
    print("你是老年")