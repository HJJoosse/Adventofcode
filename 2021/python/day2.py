

def solvepart1(content):
    coord = [0,0]

    for x in content:
        if x[0] == 'forward':
            coord[0] += x[1]
        elif x[0] == "up":
            coord[1] -= x[1]
        else: 
            coord[1] += x[1]

    return coord[1]*coord[0]

def solvepart2(content):
    coord = [0,0,0]
    
    for x in content:
        if x[0] == 'forward':
            coord[0] += x[1]
            coord[1] += x[1]*coord[2]
        elif x[0] == "up":
            coord[2] -= x[1]
        else:
            coord[2] += x[1]

    return coord[1]*coord[0]


if __name__ == "__main__":

    with open("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d2.txt","r") as f:
        content = f.read().split("\n",)[:-1]
        content = [x.split() for x in content]
        content = [[str(x[0]),int(x[1])]  for x in content]

    print(solvepart1(content))
    print(solvepart2(content))

