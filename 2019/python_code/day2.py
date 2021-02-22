def solve_part1(inputs: list,repl1: int,repl2: int):
    i = 0
    inputs[1:3] = [repl1,repl2]
    while inputs[i] != 99:
        if inputs[i] == 1:
            inputs[inputs[i+3]] = inputs[inputs[i+1]]+inputs[inputs[i+2]]
        elif inputs[i] == 2:
            inputs[inputs[i+3]] = inputs[inputs[i+1]]*inputs[inputs[i+2]]
        else:
            raise ValueError(f"{inputs[i]} is not a command")
        i+=4
    return inputs[0]

def solve_part2(inputs: list):
    for x in range(0,100):
        for y in range(0,100):
            parse_list = inputs.copy()
            if solve_part1(parse_list,x,y) == 19690720:
                return (x*100)+y

if __name__ == "__main__":
    with open("/Users/hjjoosse/Documents/UMCU/Adventofcode/2019/inputs/input_d2") as f:
        content = [int(x) for x in f.read().split(",")]
    print(solve_part1(content.copy(),12,2))
    print(solve_part2(content))