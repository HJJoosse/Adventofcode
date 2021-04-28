pos_or_im = lambda x,y,z:int(x[int(y)]) if z == "0" else int(y)

class IntCode:

    def __init__(self,inputs: list,):   
        self.indexer = 0
        self.inputs = inputs
        self.instructs = {
        "01": lambda x,y,c,b: str(int(x[pos_or_im(x,y+1,c)])+int(x[pos_or_im(x,y+2,b)])),
        "02": lambda x,y,c,b: str(int(x[pos_or_im(x,y+1,c)])*int(x[pos_or_im(x,y+2,b)])),
        "05": lambda x,y,c,b: int(x[pos_or_im(x,y+2,b)]) if x[pos_or_im(x,y+1,c)] != "0" else y+3,
        "06": lambda x,y,c,b: int(x[pos_or_im(x,y+2,b)]) if x[pos_or_im(x,y+1,c)] == "0" else y+3,
        "07": lambda x,y,c,b: 1 if int(x[pos_or_im(x,self.indexer+1,c)]) < int(inputs[pos_or_im(inputs,self.indexer+2,b)]) else 0,
        "08": lambda x,y,c,b: 1 if int(x[pos_or_im(x,self.indexer+1,c)]) == int(inputs[pos_or_im(inputs,self.indexer+2,b)]) else 0
        }
        self.outputcodes = []
        
        
    def __call__(self,phase,amplifier=None):
        
        while not self.inputs[self.indexer].endswith("99"):
            self.inputs[self.indexer] = ("0000"+self.inputs[self.indexer])[-5:]
            DE = self.inputs[self.indexer][-2:]
            C = self.inputs[self.indexer][2]
            B = self.inputs[self.indexer][1]
            A = self.inputs[self.indexer][0]
            if DE in ["01","02"]:
                self.inputs[pos_or_im(self.inputs,self.indexer+3,A)] = self.instructs[DE](self.inputs,self.indexer,C,B)
                self.indexer+=4
            elif DE == "03":
                if amplifier is not None:
                    self.inputs[pos_or_im(self.inputs,self.indexer+1,C)] = str(phase)
                    phase = amplifier
                else:
                    self.inputs[pos_or_im(self.inputs,self.indexer+1,C)] = str(phase)
                self.indexer+=2
            elif DE == "04":
                self.outputcodes.append(self.inputs[pos_or_im(self.inputs,self.indexer+1,C)])
                self.indexer+=2
                return self.inputs[self.indexer], int(self.outputcodes[-1])
            elif DE in ["05","06"]:
                self.indexer = self.instructs[DE](self.inputs,self.indexer,C,B)
            elif DE in ["07","08"]:
                self.inputs[pos_or_im(self.inputs,self.indexer+3,A)] = str(self.instructs[DE](self.inputs,self.indexer,C,B))
                self.indexer+=4
            else: 
                raise ValueError("Invalid command")
        return self.inputs[self.indexer], int(self.outputcodes[-1])