import re  # 引入正则表达式
import os

def cleanUnneeded(filename):
    input_file_dir = os.path.join("data", "original")
    output_file_dir = os.path.join("data", "derived")
    input_file_path = os.path.join(input_file_dir, filename)
    output_file_path = os.path.join(output_file_dir, filename)
    if not os.path.exists(output_file_dir):
        os.makedirs(output_file_dir)

    with open(input_file_path, "r") as f:
        lines = f.readlines()
    # 定义一个新列表来存储处理后的数据
    nocor_lines = []
    # 遍历原始文件中的每一行
    for line in lines:
        # 使用正则表达式匹配并移除 X= Y= Z=
        nocor_line = re.sub(r"X=|Y=|Z=", "", line)
        nocor_lines.append(nocor_line)

    derived_lines = [line for line in nocor_lines if '-nan' not in line]
    with open(output_file_path, "w") as f:
        f.writelines(derived_lines)
