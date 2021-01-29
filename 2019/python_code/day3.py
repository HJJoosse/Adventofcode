import operator
from collections import Counter

def x_or_y(direction:str,distance:int,last_pos:list):
    if direction in ["L","R"]:
        if direction == "R":
            x_coords = [last_pos[0]+z for z in range(1,distance+1)]
        else:
            x_coords = [last_pos[0]-z for z in range(1,distance+1)]
        y_coords = [last_pos[1]]*len(x_coords)
    
    else:
        if direction == "U":
            y_coords = [last_pos[1]+z for z in range(1,distance+1)]
        else:
            y_coords = [last_pos[1]-z for z in range(1,distance+1)]
        x_coords = [last_pos[0]]*len(y_coords)
    
    return [(x,y) for x,y in zip(x_coords,y_coords)]

def create_route(wire: list, route:dict, counter:Counter, index: int):
    direction = wire[0][0]
    distance = wire[0][1]
    wire = wire[1:]
    last_pos = route[index][-1]
    
    index += 1
    route.update({index:x_or_y(direction,distance,last_pos)})
    counter.update(route[index])
    
    return route, wire,index 

def get_euclidean(intup : tuple):
    return sum([abs(x) for x in intup])

def track_route(wire_one: list, wire_two: list,route_one: dict, route_two: list,index_a:int = 0,steps_b:int = 0):
    ct = Counter()
    while (len(wire_one) > 0):
        route_one, wire_one, index_a = create_route(wire_one, route_one, ct,index_a)
    overlap = []

    for x in wire_two:
        route_two = x_or_y(x[0],x[1],route_two[-1])
        for coord in route_two:
            steps_b +=1
            if coord in ct.keys():
                step_on_a = list(ct.keys()).index(coord)+1  
                overlap.append([get_euclidean(coord),step_on_a+steps_b])
    return overlap

if __name__ == "__main__":
    with open("../inputs/input_d3","r") as f:
       wire_one, wire_two = f.read().split("\n")[0:2]
    #wire_one = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    #wire_two = "U62,R66,U55,R34,D71,R55,D58,R83"
    wire_one = [(x[0],int(x[1:])) for x in wire_one.split(",")]
    wire_two = [(x[0],int(x[1:])) for x in wire_two.split(",")]
    intersects = (track_route(wire_one,wire_two,{0:[(0,0)]},[(0,0)]))
    print("Answer part 1:",min([x[0] for x in intersects]))
    print("Answer part 2:",min([x[1] for x in intersects]))
