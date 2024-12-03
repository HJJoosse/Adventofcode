def read_input(path:str) -> list[str]:
    with open(path,'r') as f:
        data = f.read().split("\n")[:-1]
    return data

def make_ints(in_data:list) -> list[list]:
    out_data = [x.split() for x in in_data]
    out_data = [[int(y) for y in x] for x in out_data]
    return out_data

def compare_sorted(code:list):
    return (sorted(code) == code) or (sorted(code,reverse=True) == code)

def is_safe(code:list):
    sums = [abs(code[x]-code[x+1]) for x in range(len(code)-1)]
    return (max(sums) <= 3) & (min(sums) > 0)

def count_safe_codes(int_data:list,damper = False) -> int:
    safe_code_count = 0
    for code in int_data:
        if compare_sorted(code) & is_safe(code):
            safe_code_count += 1
        else:
            if damper:
                for i in range(len(code)):
                    code_new = code.copy()
                    code_new.pop(i)
                    if compare_sorted(code_new) & is_safe(code_new):
                        safe_code_count += 1
                        break
            continue
    return safe_code_count

if __name__ == "__main__":
    DATA_PATH = "/Users/hjjoosse/Documents/UMCU/Adventofcode/aoc2024/data/input-day2.txt"
    input_data = read_input(DATA_PATH)
    # input_data = ["7 6 4 2 1","1 2 7 8 9","9 7 6 2 1","1 3 2 4 5","8 6 4 4 1","1 3 6 7 9"]
    int_data = make_ints(input_data)
    print(count_safe_codes(int_data,damper=False)) ## part 1
    print(count_safe_codes(int_data,damper=True)) ## part 1
