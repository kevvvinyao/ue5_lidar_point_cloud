import re  # 引入正则表达式
import os

# 定义原始点云文件路径
original_file_path = os.path.join("data", "original.txt")

# 定义新文本文件路径
new_file_path = os.path.join("data", "new.txt")

# 读取原始点云文件
with open(original_file_path, "r") as f:
    lines = f.readlines()

# 定义一个新列表来存储处理后的数据
new_lines = []

# 遍历原始文件中的每一行
for line in lines:
    # 使用正则表达式匹配并移除 X= Y= Z=
    new_line = re.sub(r"X=|Y=|Z=", "", line)

    # 将新的行添加到 new_lines 列表中
    new_lines.append(new_line)

# 将处理后的数据写入新的文本文件
with open(new_file_path, "w") as f:
    f.writelines(new_lines)

