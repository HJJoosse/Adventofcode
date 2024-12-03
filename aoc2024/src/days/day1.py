path = "/Users/hjjoosse/Documents/UMCU/Adventofcode/aoc2024/data/input_day1.txt"
with open(path,"r", encoding='utf-8') as f:
    data = f.read().split("\n")[:-1] ### somehow always whitespace
left = sorted([int(x.split()[0]) for x in data])
right = sorted([int(x.split()[1]) for x in data])

print(sum(abs(x-y) for x,y in zip(left,right))) ## part 1
print(sum(x*right.count(x) for x in left)) ## part 2
