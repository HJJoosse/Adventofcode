
if __name__ == "__main__":
    with open("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d7.txt","r") as f:
        positions = [int(x) for x in f.read().split(",")]

    #positions = [16,1,2,0,4,2,7,1,2,14]
    print(min([sum([abs(x-y) for x in positions]) for y in range(0,max(positions))]))
    print(min([sum([sum([x for x in range(z+1)]) for z in [abs(e-y) for e in positions]]) for y in range(1,max(positions)+1)]))