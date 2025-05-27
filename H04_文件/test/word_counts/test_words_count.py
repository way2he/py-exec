import re

def count_words_in_file(source_path: str, target_path: str) -> None:
    """
    统计源文件中每个单词的出现次数，并将结果写入目标文件

    参数:
        source_path (str): 源文本文件路径
        target_path (str): 目标结果文件路径
    """
    try:
        # 读取源文件内容
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 文本预处理：转换为小写，去除标点，分割单词
        # 使用正则表达式匹配非字母数字字符作为分隔符
        words = re.findall(r'\b\w+\b', content.lower())
        
        # 统计单词频率（使用字典手动计数）
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1  # 若单词不存在则初始化为0，否则加1
        
        # 格式化统计结果
        result_lines = [f"{word}: {count}" for word, count in word_counts.items()]  # 遍历字典键值对
        result_content = '\n'.join(result_lines)
        
        # 写入目标文件
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(result_content)
        
        print(f"统计完成，结果已写入 {target_path}")
    except Exception as e:
        print(f"发生未知错误：{str(e)}")


# 示例用法（根据实际路径调整）
if __name__ == "__main__":
    count_words_in_file("source.txt", "word_counts.txt")