from day5 import solve_part2
import itertools


if __name__ == "__main__":
    with open("2019/inputs/input_d7",'r') as f:
        content = f.read().split(",")
    #content = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0".split(",")
    print(content)
    ranges = [0,1,2,3,4]
    phase_settings = [x for x in itertools.permutations(range(5))]
    out_vals = []
    for setting in phase_settings:
        amplifier = 0
        for phase in setting:    
            temp_content = content.copy()
            amplifier = solve_part2(temp_content,phase,amplifier)
        out_vals.append(amplifier)

    print(max(out_vals))
    print(phase_settings[out_vals.index(max(out_vals))])