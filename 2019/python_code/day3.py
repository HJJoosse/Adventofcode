import operator

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

def create_route(wire: list, route:list, steps: int):
    direction = wire[0][0]
    distance = wire[0][1]
    wire = wire[1:]
    last_pos = route[-1]
    route += x_or_y(direction,distance,last_pos)
    steps += 1
    return route, wire,steps 

def get_euclidean(intup : tuple):
    return sum([abs(x) for x in intup])

def track_route(wire_one: list, wire_two: list,route_one: list, route_two: list,steps_a:int = 0,steps_b:int = 0):
    while (len(wire_one) > 0):
        route_one, wire_one, steps_a = create_route(wire_one, route_one,steps_a)
    overlap = []

    for x in wire_two:
        route_two = x_or_y(x[0],x[1],route_two[-1])
        for coord in route_two:
            steps_b +=1
            if coord in route_one:
                step_on_a = route_one.index(coord)
                overlap.append([get_euclidean(coord),step_on_a+steps_b])
    return overlap

if __name__ == "__main__":
    with open("../inputs/input_d3","r") as f:
       wire_one, wire_two = f.read().split("\n")[0:2]
    #wire_one = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    #wire_two = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    wire_one = [(x[0],int(x[1:])) for x in wire_one.split(",")]
    wire_two = [(x[0],int(x[1:])) for x in wire_two.split(",")]
    intersects = (track_route(wire_one,wire_two,[(0,0)],[(0,0)]))
    print(min([x[0] for x in intersects]))
    print(min([x[1] for x in intersects]))
