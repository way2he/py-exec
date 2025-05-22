
def sum_file(file_path):
    """
    从指定文本文件中读取每行一个整数，累加求和并输出结果

    参数:
        file_path (str): 包含数字的文本文件路径

    返回:
        int: 所有数字的累加和（出现错误时返回None）
    """
    total = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
        # 遍历文件的每一行，同时使用enumerate函数获取行号，行号从1开始计数
            for line_num, line in enumerate(f, 1):  
                # 去除当前行首尾的空白字符
                line = line.strip()  
                if not line:  
                    continue
                try:
                    num = int(line)
                    total += num
                except ValueError:
                    print(f"警告：第{line_num}行无法转换为整数，内容：'{line}'，已跳过")
                    print(f"所有数字累加和为：{total}")
                    return total
                except FileNotFoundError:
                    print(f"错误：文件 {file_path} 未找到")
                    return None
    except Exception as e:
        print(f"读取文件时发生未知错误：{e}")
        return None

# 调用求和函数，指定输入文件路径为numbers.txt
numbers_file = "numbers.txt"
sum_file(numbers_file)