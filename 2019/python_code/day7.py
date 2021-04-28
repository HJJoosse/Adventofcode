from intcode import IntCode
import sys
import itertools
from time import sleep

if __name__ == "__main__":
    with open("2019/inputs/input_d7",'r') as f:
        content = f.read().split(",")
    #content = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10".split(",")
    

    def part_1(content):
        phase_settings = [x for x in itertools.permutations(range(5))]
        out_vals = []
        for setting in phase_settings:
            amplifier = 0
            
            for phase in setting:    
                temp_content = content.copy()
                amplifier = IntCode(temp_content)(phase,amplifier)[-1]
            out_vals.append(amplifier)
        return out_vals

    def run_amplifiers(phases):
        amp_list = [0,0,0,0,0]
        int_codes = [IntCode(content.copy()) for i in range(len(phases))]
        iterations = 0
        while True:
            
            for ix,phase in enumerate(phases):
                if iterations != 0:
                    code, output = int_codes[ix](phase = amp_list[ix])
                else:
                    code, output = int_codes[ix](phase,amp_list[ix])
                if ix == 4:
                    amp_list[0] = output                                        
                    iterations+=1
                    if code[-2:] == '99':
                        return amp_list[0]
                else: 
                    amp_list[ix+1] = output
                    
                
    def part_2(content):       
        init_phases = [x for x in itertools.permutations(range(5,10))]
        out_vals = []
        for phases in init_phases:
            out_vals.append(run_amplifiers(phases))
        
        return out_vals

    print(max(part_2(content)))