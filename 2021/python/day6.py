from collections import Counter

def countdown(countdowns:list,days:int):
    count_dict = Counter(countdowns)
    for _ in range(days):
        new_dict = {k:0 for k in range(0,8)}
        for k,v in count_dict.items():
            if k != 0:
                new_dict[k-1] += v
                
            else:
                new_dict[8] = v
                new_dict[6] += v

        count_dict = new_dict

    return sum([v for v in count_dict.values()])

if __name__ == "__main__":
    with open("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d6.txt",'r') as f:
        content = [int(x) for x in f.read().split(",")]

    #content = [int(x) for x in "3,4,3,1,2".split(",")]

    print(countdown(content,80))
    print(countdown(content,256))