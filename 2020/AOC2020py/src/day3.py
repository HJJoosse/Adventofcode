import numpy as np
import re

class TreeCounter():
    """Count trees in a field"""

    def __init__(self,content: str):
        self.content = content
        self.movements = [[1,1],[3,1],[5,1],[7,1],[1,2]]

    def split_inputs(self):
        self.content = re.split('\n', self.content)
        self.content = np.array([re.findall('.{1}', x) for x in self.content if len(x) > 1])

    def tree_counter(self,x_mov,y_mov):
        x = 0
        y = 0
        trees = 0

        while (y < len(self.content)):
            if self.content[y,x] == '#':
                trees+=1
            y+=y_mov
            x+=x_mov
            if x >= len(self.content[0, :]):
                x = x % len(self.content[0, :])
        return trees

    def make_total_sum(self):
        trees = 1
        for x, y in self.movements:
            trees *= self.tree_counter(x, y)
        return trees


if __name__ == '__main__':

    with open('resources/input_d3','r') as f:
        content = f.read()
    tc = TreeCounter(content=content)
    tc.split_inputs()
    print(tc.make_total_sum())


