from typing import ValuesView


def solvepart1(depths:list):
    count = sum(find_low_points(depths).values())
    return count

def find_low_points(depths:list):
    low_points = {}
    for i in range(len(depths)):
        for j in range(len(depths[i])):
            height = depths[i][j]
            surroudings = []
            for x,y in [[i-1,j],[i+1,j],[i,j+1],[i,j-1]]:
                if (x < 0) | (y < 0) | (y>(len(depths[i])-1)) | (x>(len(depths))-1):
                    pass
                else:
                    surroudings.append(depths[x][y])
            if all([height < x for x in surroudings]):
                low_points.update({(i,j):(1+height)})
    return low_points

def get_basin(depths, coord, visited):
    x,y = coord
    neighbors = [(x-1,y),(x+1,y),(x,y+1),(x,y-1)]
    for nn in neighbors:
        new_coords = update_visited(depths, nn, visited)
        if new_coords != None:
            visited.update(new_coords)
    return visited

def update_visited(depths, nn, visited):
    x,y = nn
    if (x < 0) | (y < 0) | (x>(len(depths))-1) | (y>(len(depths[0])-1)):
        return visited
    elif (depths[x][y] == 9) | (nn in visited):
        return visited
    else: 
        visited.add(nn)
        get_basin(depths, nn, visited)  

def solvepart2(depths:list):
    low_points = find_low_points(depths)
    basins = [0,0,0]
    for low_point in low_points.keys():
        visited = set([low_point])
        basins.append(len(get_basin(depths,low_point,visited)))
    
    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]


if __name__ == "__main__":
    with open("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d9.txt","r") as f:
        depths = [x for x in f.read().split("\n")]
        for i in range(len(depths)):
            depths[i] = [int(x) for x in depths[i]]
        
        
    print(solvepart1(depths))
    print(solvepart2(depths))