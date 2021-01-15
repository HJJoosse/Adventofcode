def fuel_adder(fuel: int):
    return (fuel//3)-2


# Part 1
def d1_part1(file: str):
    total_sum = 0
    with open(file) as f:
        total_sum = sum([fuel_adder(int(line)) for line in f.read().split()])
    return total_sum


# Part 2
def d1_part2(file: str):
    total_sum = 0
    with open(file) as f:
        for line in f.read().split():
            line_sum = fuel_adder(int(line))
            fuel_to_add = fuel_adder(line_sum)
            line_sum += fuel_to_add
            while fuel_adder(fuel_to_add) > 0:
                fuel_to_add = fuel_adder(fuel_to_add)
                line_sum += fuel_to_add
            total_sum += line_sum
    return total_sum


