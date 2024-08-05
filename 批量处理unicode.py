import os

def get_all_txt_filepaths_in_directory(directory):
    # 确保提供的路径是一个目录
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a directory.")
        return []

    # 初始化一个列表来存储所有txt文件的完整路径
    txt_filepaths = []

    # 遍历目录中的所有文件和文件夹
    for filename in os.listdir(directory):
        # 构造文件的完整路径
        filepath = os.path.join(directory, filename)
        
        # 检查文件是否是一个文件并且以.txt结尾
        if os.path.isfile(filepath) and filepath.endswith('.txt'):
            # 将文件的完整路径添加到列表中
            txt_filepaths.append(filepath)

    # 返回包含所有txt文件完整路径的列表
    return txt_filepaths

# 替换为你的目录路径
directory_path = './guan/'
txt_filepaths = get_all_txt_filepaths_in_directory(directory_path)
#对汉字进行unicode编码
def chinese_to_unicode_html(content):
    # 使用列表推导式和ord()函数获取每个字符的Unicode码点，然后转换为HTML实体编码
    return ''.join(f'&#{ord(char)};' for char in content) 
with open('output.txt', 'w', encoding='utf-16') as outfile:
    # 遍历文件名列表
    for name in txt_filepaths:
        # 使用with open打开每个文件，并读取内容
        with open(name, 'r', encoding='utf-16') as infile:
            for line in infile:
                encoded_text = chinese_to_unicode_html(line)
                # 这里我们简单地将"%10;"替换为"\n"（仅换行）
                modified_content = encoded_text.replace("&#10;", "\n")
                # 将修改后的内容写入到新的文件
                outfile.write(modified_content)
                print("文件处理完成，结果已保存到output.txt中。")