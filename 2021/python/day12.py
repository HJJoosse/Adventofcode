
def makehashmap(directions:list) -> dict:
    cave_map = dict()
    for k,v in directions:
        if k in cave_map:
            cave_map[k].append(v)
        else:
            cave_map.update({k:[v]})
        if v in cave_map:
            cave_map[v].append(k)
        else:
            cave_map.update({v:[k]})
    return cave_map
    
def find_routes(cave_map:dict,visited:list,start:str,routes:int):
    for cave in cave_map[start]:
        if cave == 'end':
            return 1
        elif cave.isupper() | (cave.islower() & (cave not in visited)):
            visited_new = visited.copy()
            visited_new.append(cave)
            routes += find_routes(cave_map,visited_new,cave,routes)
        else: return 0



if __name__ == "__main__":
    
    with open('/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d12.txt','r') as f:
        directions = [x.split('-') for x in f.read().split('\n')]
    cave_map = makehashmap(directions=directions)    
    print(find_routes(cave_map,[],'start',0))