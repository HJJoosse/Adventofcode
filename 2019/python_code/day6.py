def orbit_mapper(orbits_list: list):
    orbits_split = [x.split(")") for x in orbits_list]
    orbits = {}
    for inner,outer in orbits_split:
        if inner not in orbits.keys():
            orbits[inner] = [outer]
        else:
            orbits[inner].append(outer)
    return orbits

def orbit_counter(orbits: dict):
    orbit_map = [("COM",0)]
    for inner,counter in orbit_map:
        try:
            for outer in orbits[inner]:
                orbit_map.append((outer,counter+1))
        except KeyError:
            continue
    return orbit_map

if __name__ ==  "__main__":
    with open("../inputs/input_d6",'r') as f:
        content = f.read().split("\n")[:-1]

    #content = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L".split("\n")
    print(sum([x[1] for x in orbit_counter(orbit_mapper(content))]))
