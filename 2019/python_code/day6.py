def orbit_mapper(orbits_list: list):
    orbits_split = [x.split(")") for x in orbits_list]
    orbit_map = {}
    for inner,outer in orbits_split:
        if inner not in orbit_map.keys():
            orbit_map[inner] = [outer]
        else:
            orbit_map[inner].append(outer)
    return orbit_map

def orbit_counter(orbit_map: dict):
    orbit_counter = [("COM",0)]
    for inner,counter in orbit_counter:
        try:
            for outer in orbit_map[inner]:
                orbit_counter.append((outer,counter+1))
        except KeyError:
            continue
    return orbit_counter

def move_around(orbit_map: dict):
    counter = 0
    outers = list(orbit_map.values())
    inners = list(orbit_map.keys())

    searcher = "SAN"

    path_to_start = []
    while searcher not in orbit_map["COM"]:
        searcher = inners[outers.index([x for x in outers if searcher in x][0])]
        path_to_start.append(searcher)

    pos = inners[outers.index([x for x in outers if "YOU" in x][0])]
    while pos not in path_to_start:
        pos = inners[outers.index([x for x in outers if pos in x][0])]
        counter += 1

    return counter + path_to_start.index(pos)

if __name__ ==  "__main__":
    with open("../inputs/input_d6",'r') as f:
        content = f.read().split("\n")[:-1]

    #content = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN".split("\n")
    print(sum([x[1] for x in orbit_counter(orbit_mapper(content))]))
    print(move_around(orbit_mapper(content)))