with open("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d1.txt","r") as f:
    content = [int(x) for x in f.read().split()]

print(sum([content[i+1]>content[i] for i in range(len(content)-1)]))

print(sum([sum(content[i:i+3]) < sum(content[i+1:i+4]) for i in range(len(content)) if (len(content[i:i+3]) ==3) & (len(content[i+1:i+4])==3)]))