def filter_nan(input_file, output_file):
    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()

    filtered_lines = [line for line in lines if '-nan' not in line]

    with open(output_file, 'w') as f_out:
        f_out.writelines(filtered_lines)


# 使用示例
input_file = 'input.txt'
output_file = 'output.txt'
filter_nan(input_file, output_file)