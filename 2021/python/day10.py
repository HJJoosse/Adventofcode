def solvepart1(syntaxes):
    open_chunk = ['[','{','<','(']
    close_chunk = [']','}','>',')']
    map_dict = {k:v for k,v in zip(open_chunk,close_chunk)}
    val_dict = {')':3,']':57,'}':1197,'>':25137}
    error_val = 0
    for line in syntaxes:
        stack = []
        for x in line:
            if x in open_chunk:
                stack.append(x)
            else:
                if x != map_dict[stack.pop()]:
                    error_val += val_dict[x]
                    break

    return error_val
                
def check_line(line, map_dict):   
    stack = []
    for x in line:      
        if x in map_dict.keys():
            stack.append(x)
        elif x != map_dict[stack.pop()]:
            return []
    return stack     


def solvepart2(syntaxes):
    open_chunk = ['[','{','<','(']
    close_chunk = [']','}','>',')']
    map_dict = {k:v for k,v in zip(open_chunk,close_chunk)}
    value_dict = {']':2,')':1,'}':3,'>':4}
    completion_scores = []
    for line in syntaxes:
        stack = check_line(line, map_dict)                          
        if len(stack) == 0:
            continue
        else:
            completion_score = 0
            while len(stack) > 0:
                completion_score = (completion_score * 5) + value_dict[map_dict[stack.pop()]]
        completion_scores.append(completion_score)
    return sorted(completion_scores)[int(len(completion_scores)/2)]
                
                


with open("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d10.txt",'r') as f:
    content = f.read().split("\n")

print(solvepart2(content))