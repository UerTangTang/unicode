import os

# 初始化一个列表来存储所有txt文件的文件名
txt_filenames = []
#读取文件夹下面所有txt文件
def get_all_txt_filenames_in_directory(directory):
    # 确保提供的路径是一个目录
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a directory.")
        return []
    # 遍历目录中的所有文件和文件夹
    for filename in os.listdir(directory):
        # 构造文件的完整路径（这里不需要，因为我们只关心文件名）
        # 但我们可以使用它来检查文件扩展名
        filepath = os.path.join(directory, filename)
        
        # 检查文件是否是一个文件并且以.txt结尾
        if os.path.isfile(filepath) and filepath.endswith('.txt'):
            # 将文件名添加到列表中
            txt_filenames.append(filename)
    # 返回包含所有txt文件名的列表
    return txt_filenames
# 替换为你的目录路径
directory_path = './guan'
txt_filenames = get_all_txt_filenames_in_directory(directory_path)
#对汉字进行unicode编码
def chinese_to_unicode_html(content):
    # 使用列表推导式和ord()函数获取每个字符的Unicode码点，然后转换为HTML实体编码
    return ''.join(f'&#{ord(char)};' for char in content) 
with open('output.txt', 'w', encoding='utf-16') as outfile:
    # 遍历文件名列表
    for filename in txt_filenames:
        # 使用with open打开每个文件，并读取内容
        with open(filename, 'r', encoding='utf-16') as infile:
            for line in infile:
                encoded_text = chinese_to_unicode_html(line)
                # 这里我们简单地将"%10;"替换为"\n"（仅换行）
                modified_content = encoded_text.replace("&#10;", "\n")
                # 将修改后的内容写入到新的文件
                outfile.write(modified_content)
                print("文件处理完成，结果已保存到output.txt中。")