def solvePart1(content):
    gamma = None
    epsilon = None
    for i in range(len(content[0])):
        if gamma == None:
            gamma = "1" if sum([int(x[i]) for x in content]) > len([x[i] for x in content])/2 else "0"
            epsilon = "0" if sum([int(x[i]) for x in content]) > len([x[i] for x in content])/2 else "1"
        else:
            gamma += "1" if sum([int(x[i]) for x in content]) > len([x[i] for x in content])/2 else "0"
            epsilon += "0" if sum([int(x[i]) for x in content]) > len([x[i] for x in content])/2 else "1"
    
    gamma = sum([2**i * int(gamma[-i-1]) for i in range(len(gamma))])
    epsilon = sum([2**i * int(epsilon[-i-1]) for i in range(len(epsilon))])
    return gamma * epsilon


def solvePart2(content):
    oxygen_generator = content.copy()
    co2_scrub = content.copy()
    i=0
    while len(oxygen_generator)!=1:
        most_common = "1" if sum([int(x[i]) for x in oxygen_generator]) >= len([x[i] for x in oxygen_generator])/2 else "0"
        oxygen_generator = [x for x in oxygen_generator if x[i] == most_common]
        i+=1
    i = 0
    while len(co2_scrub) != 1:
        least_common = "0" if sum([int(x[i]) for x in co2_scrub]) >= len([x[i] for x in co2_scrub])/2 else "1"
        co2_scrub = [x for x in co2_scrub if x[i] == least_common]
        i+=1

    oxygen_generator = sum([2**i * int(oxygen_generator[0][-i-1]) for i in range(len(oxygen_generator[0]))])
    co2_scrub = sum([2**i * int(co2_scrub[0][-i-1]) for i in range(len(co2_scrub[0]))])
    
    return  oxygen_generator*co2_scrub


if __name__ == "__main__":
    with open("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d3.txt","r") as f:
        content = f.read().split("\n")[:-1]

    print(solvePart1(content))
    print(solvePart2(content))

        