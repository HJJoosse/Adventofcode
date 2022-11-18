

def solvepart1(digits):
    count = 0
    for inp,outp in digits:
        for word in outp.split(" "):
            if len(word) in [2,4,3,7]:
                count += 1

    return count

def solvepart2(digits):
    outputs = []
    for inp,outp in digits:
        map_dict = {}
        map_dict.update({
            1:set([y for y in [x for x in inp.split() if len(x) == 2][0]]),
            4:set([y for y in [x for x in inp.split() if len(x) == 4][0]]),
            7:set([y for y in [x for x in inp.split() if len(x) == 3][0]]),
            8:set([y for y in [x for x in inp.split() if len(x) == 7][0]]),})
        output_str = ""
        for word in outp.split():
            word = [x for x in word]
            if set(word) in map_dict.values():
                output_str += str([k for k,v in map_dict.items() if set(word) == v][0])
            elif (len(word) == 6):
                if map_dict[1] <= set(word):
                    if map_dict[4] <= set(word):
                        output_str += "9"
                    else: output_str += "0"
                else: output_str += "6"

            elif len(word) == 5:
                if map_dict[1] <= set(word):
                    output_str += "3"
                elif {x for x in map_dict[4] if x not in map_dict[7]} <= set(word):
                    output_str += "5"
                else: output_str += "2"
        outputs.append(int(output_str))
    return sum(outputs)

if __name__ == "__main__":
    with open("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d8.txt","r") as f:
        digits = f.read().split("\n")
        digits = [x.split("|") for x in digits]

    print(solvepart1(digits))
    print(solvepart2(digits))

digits.sort()
