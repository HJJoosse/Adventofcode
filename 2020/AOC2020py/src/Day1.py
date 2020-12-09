import re

with open('input_d1','r') as f:
    content = f.read()

numbers_list = sorted([int(x) for x in re.findall('\d+',content)])

for val in numbers_list:
    rest = 2020 - val
    if rest in [x for x in numbers_list if x > val]:
        print(rest*val)