
def SolverPart1(coords_list):
    x_len = max([y[0] for x in coords_list for y in x])
    y_len = max([y[1] for x in coords_list for y in x])
    field = []
    for i in range(y_len+1):
        field.append([0]*(x_len+1))
    for start,end in coords_list:
        if start[1] == end[1]:  
            min_x = min([end[0],start[0]]) 
            max_x = max([end[0],start[0]])
            field[start[1]][min_x:max_x+1] = [x + 1 for x in field[start[1]][min_x:max_x+1]]
        elif start[0] == end[0]:
            min_y = min([end[1],start[1]])
            max_y = max([end[1],start[1]])
            for y in range(min_y,max_y+1):
                field[y][start[0]] += 1
    s = 0
    for i in range(y_len+1):
        s+= sum([x > 1 for x in field[i]])

    return(s)
    

def SolverPart2(coords_list):
    x_len = max([y[0] for x in coords_list for y in x])
    y_len = max([y[1] for x in coords_list for y in x])
    field = []
    for i in range(y_len+1):
        field.append([0]*(x_len+1))
    for start,end in coords_list:
        if start[1] == end[1]:  
            min_x = min([end[0],start[0]]) 
            max_x = max([end[0],start[0]])
            field[start[1]][min_x:max_x+1] = [x + 1 for x in field[start[1]][min_x:max_x+1]]
        elif start[0] == end[0]:
            min_y = min([end[1],start[1]])
            max_y = max([end[1],start[1]])
            for y in range(min_y,max_y+1):
                field[y][start[0]] += 1
        else:
            
            direction_x = -1 if start[0] > end[0] else 1
            direction_y = -1 if start[1] > end[1] else 1
            coords_update = [[x,y] for x,y in zip(range(start[0],end[0]+direction_x,direction_x),range(start[1],end[1]+direction_y,direction_y))]
            for coord in coords_update:
                field[coord[1]][coord[0]] +=1 
    s = 0
    for i in range(y_len+1):
        s+= sum([x > 1 for x in field[i]])

    return(s)
     

if __name__ == "__main__":
    with open("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d5.txt",'r') as f:
        content = f.read().split("\n")[:-1]
        coords = []
        for dir in content:
            
            coords.append([(int(y.split(",")[0]),int(y.split(",")[1])) for y in dir.split("->")])
    print("part 1: "+str(SolverPart1(coords)))
    print("part 2: "+str(SolverPart2(coords)))