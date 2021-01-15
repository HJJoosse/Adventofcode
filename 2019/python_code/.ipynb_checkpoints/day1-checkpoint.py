#Part 1
def d1_part1(file: str):
    total_sum = 0
    with open(file) as f:
        total_sum = sum[(int(line)//3)-2 for line in f.read().split()]
    return total_sum

# Part 2
def fuel_adder(fuel: int):
    return (fuel//3)-2

def d1_part2(file: str):
    init_fuel = d1_part1(file)
    fuel_to_add = fuel_adder(init_fuel)
    total_fuel = fuel_to_add+init_fuel
    print(total_fuel)
    while fuel_to_add > 0:
        total_fuel+=fuel_adder(fuel_to_add)
    return total_fuel