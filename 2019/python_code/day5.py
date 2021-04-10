pos_or_im = lambda x,y,z:int(x[int(y)]) if z == "0" else int(y)

def solve_part1(inputs: list,*args,**kwargs):
    i = 0
    outputcodes = []
    diag_code = 1
    while not inputs[i].endswith("99"):
        inputs[i] = ("0000"+inputs[i])[-5:]
        C = inputs[i][2]
        B = inputs[i][1]
        if inputs[i].endswith("01"):
            inputs[int(inputs[i+3])] = str(int(inputs[pos_or_im(inputs,i+1,C)])+int(inputs[pos_or_im(inputs,i+2,B)]))
            i+=4
        elif inputs[i].endswith("02"):
            inputs[int(inputs[i+3])] = str(int(inputs[pos_or_im(inputs,i+1,C)])*int(inputs[pos_or_im(inputs,i+2,B)]))
            i+=4
        elif inputs[i].endswith("03"):
            inputs[pos_or_im(inputs,i+1,C)]  = str(diag_code)
            i+=2
        elif inputs[i].endswith("04"):
            outputcodes.append(inputs[pos_or_im(inputs,i+1,C)])
            i+=2
        else: continue
    return outputcodes[-1]
    
def solve_part2(inputs: list,*args,**kwargs):
    i = 0
    outputcodes = []
    instructs = {
        "01": lambda x,y,c,b: str(int(x[pos_or_im(x,y+1,c)])+int(x[pos_or_im(x,y+2,b)])),
        "02": lambda x,y,c,b: str(int(x[pos_or_im(x,y+1,c)])*int(x[pos_or_im(x,y+2,b)])),
        "05": lambda x,y,c,b: int(x[pos_or_im(x,y+2,b)]) if x[pos_or_im(x,y+1,c)] != "0" else y+3,
        "06": lambda x,y,c,b: int(x[pos_or_im(x,y+2,b)]) if x[pos_or_im(x,y+1,c)] == "0" else y+3,
        "07": lambda x,y,c,b: 1 if int(x[pos_or_im(x,i+1,c)]) < int(inputs[pos_or_im(inputs,i+2,b)]) else 0,
        "08": lambda x,y,c,b: 1 if int(x[pos_or_im(x,i+1,c)]) == int(inputs[pos_or_im(inputs,i+2,b)]) else 0
    }
    diag_codes = [x for x in args+tuple(kwargs.values())]
    diag_code_indexer = 0
    while not inputs[i].endswith("99"):
        inputs[i] = ("0000"+inputs[i])[-5:]
        
        DE = inputs[i][-2:]
        C = inputs[i][2]
        B = inputs[i][1]
        A = inputs[i][0]
        if DE in ["01","02"]:
            inputs[int(inputs[i+3])] = instructs[DE](inputs,i,C,B)
            i+=4
        if DE in ["07","08"]:
            inputs[int(inputs[i+3])] = str(instructs[DE](inputs,i,C,B))
            i+=4
        if DE in ["05","06"]:
            i = instructs[DE](inputs,i,C,B)
        elif DE == "03":
            inputs[pos_or_im(inputs,i+1,C)] = str(diag_codes[diag_code_indexer])
            diag_code_indexer+=1
            i+=2
        elif DE == "04":
            outputcodes.append(inputs[pos_or_im(inputs,i+1,C)])
            i+=2
        else: continue
    return outputcodes[-1]


if __name__ == "__main__":
    with open("2019/inputs/input_d5") as f:
        content = f.read().split(",")
    print(solve_part1(content.copy(),1))
    print(solve_part2(content,5,yolo = 2))
