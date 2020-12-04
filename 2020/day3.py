import numpy as np
import re


with open('input_d3','r') as f:
    content = f.read()



content = re.split('\n',content)
#print([x for x in content])
content = np.array([re.findall('.{1}',x) for x in content if len(x) > 1])


def tree_counter(x_mov,y_mov):
    x = 0; y = 0; trees = 0
    while (y < len(content)):
        if content[y,x] == '#':

            trees+=1
        y+=y_mov; x+=x_mov

        if (x  >= len(content[0,:])):
            x = x%len(content[0,:])
    return trees

movements = [[1,1],[3,1],[5,1],[7,1],[1,2]]
trees = 1
for x,y in movements:
    trees *= tree_counter(x,y)

print(trees)

