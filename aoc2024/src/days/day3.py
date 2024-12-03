import re
from operator import mul

def read_input(path:str) -> str:
    with open(path,'r') as f:
        data = f.read().split("\n")
    data = ''.join(data)
    return data

def multiply_code(input_data):
    codes = [eval(x) for x in re.findall(r"mul\(\d{1,3},\d{1,3}\)",input_data)]
    return sum(codes)

def multiply_code_filter(input_data):
    codes = re.findall(r"mul\(\d{1,3},\d{1,3}\)",''.join(
        re.findall(r"^.*?don't\(\)|do\(\).*?don't\(\)?|do\(\).*?$",input_data)))
    
    return sum([eval(x) for x in codes])
    
if __name__ == "__main__":
    DATA_PATH = "/Users/hjjoosse/Documents/UMCU/Adventofcode/aoc2024/data/input_day3.txt"
    input_data = read_input(DATA_PATH)
    print("part 1:",multiply_code(input_data))
    print("part 2:",multiply_code_filter(input_data))