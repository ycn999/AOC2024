import re

def file_to_text(file_path):
    with open(file_path, 'r') as file:
        txt = file.read()
    return txt

mem = file_to_text(input_file_path)

mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
instructions = re.findall(mul_pattern, mem)

add_up = 0
for i in instructions:
    mul_ints_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    find_mul_int = re.findall(mul_ints_pattern, i)
    for x,y in find_mul_int:
        add_up += (int(x)*int(y))

puzzle1 = add_up
