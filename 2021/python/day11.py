def solvepart1(charge,steps):
    flashes_no = 0
    for _ in range(steps):
        charge = [[x+1 for x in charge[i]] for i in range(len(charge))]
        flashed_points = []        
        flashes = check_flashes(charge,[],flashed_points)       
        while len(flashes) > 0:
            charge = make_flashes(charge,flashes)
            flashed_points += flashes
            flashes_no += len(flashes)
            flashes = check_flashes(charge,[],flashed_points)   
        charge = [[0 if x > 9 else x for x in charge[i]] for i in range(len(charge))]
    return flashes_no

def solvepart2(charge):
    i = 0 
    while sum([x for i in range(len(charge)) for x in charge[i]]) != 0:
        charge = [[x+1 for x in charge[i]] for i in range(len(charge))]
        flashed_points = []        
        flashes = check_flashes(charge,[],flashed_points)       
        while len(flashes) > 0:
            charge = make_flashes(charge,flashes)
            flashed_points += flashes
            flashes = check_flashes(charge,[],flashed_points)   
        charge = [[0 if x > 9 else x for x in charge[i]] for i in range(len(charge))]
        i+=1
    return i


def check_flashes(charge,flashes,flashed_points):
    for y in range(len(charge)):
        for x in range(len(charge[y])):
            if charge[y][x] > 9:
                if [y,x] not in flashed_points:
                    flashes.append([y,x])
    return flashes

def make_flashes(charge,flashes):
    for y,x in flashes:
        coords = [(y+i,x+j) for i in [-1,0,1] for j in [-1,0,1] if ((i,j) != (0,0)) & (x+j >= 0) & (y+i >= 0)]
        for yi,xj in coords:

            try:
                charge[yi][xj] += 1
            except IndexError:
                continue
    return charge

if __name__ == "__main__":
    with open("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d11.txt","r") as f:
        charge = [x for x in f.read().split("\n")]
        charge = [[int(x) for x in charge[i]] for i in range(len(charge))]
    print(charge)
    print(solvepart2(charge))