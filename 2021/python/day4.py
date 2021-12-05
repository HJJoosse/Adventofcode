def solvePart1(bingo_numbers, bingo_cards):
    bingo_cards_dict = make_bingo_dict(bingo_cards)
    bingo_numbers = [int(x) for x in bingo_numbers]
    drawn_numbers = []
    while True:
        drawn_numbers.append(bingo_numbers[0])
        bingo_numbers = bingo_numbers[1:]
        for k,v in bingo_cards_dict.items():
            for poss in v:
                if set(poss) <= set(drawn_numbers):
                    unmarked = {y for x in bingo_cards_dict[k][0:5] for y in x if not y in drawn_numbers}
                    return sum(unmarked)*list(drawn_numbers)[-1]

def solvePart2(bingo_numbers, bingo_cards):
    bingo_cards_dict = make_bingo_dict(bingo_cards)
    bingo_numbers = [int(x) for x in bingo_numbers]
    drawn_numbers = []
    completed_boards = []
    while True:
        for k in completed_boards:
            try:
                del bingo_cards_dict[k]
            except KeyError:
                continue
        drawn_numbers.append(bingo_numbers[0])
        bingo_numbers = bingo_numbers[1:]        
        for k,v in bingo_cards_dict.items():
            for poss in v:
                if set(poss) <= set(drawn_numbers):
                    if len(bingo_cards_dict.keys()) == 1:
                        unmarked = {y for x in bingo_cards_dict[k][0:5] for y in x if not y in drawn_numbers}
                        return sum(unmarked)*drawn_numbers[-1]
                    else:
                        completed_boards.append(k)
                        

def make_bingo_dict(bingo_cards):
    bingo_cards_array = []
    for i in range(len(bingo_cards)):
        bingo_cards_array.append([int(y) for x in bingo_cards[i] for y in x.split(" ") if y != '' ])
    k = 1
    bingo_dict = {}
    for arr in bingo_cards_array:
        possibilities = [arr[i*5:(i*5)+5] for i in range(5)]
        columns = [[i,i+5,i+10,i+15,i+20] for i in range(5)]
        for col in columns:
            possibilities += [[arr[i] for i in col]]
        bingo_dict.update({k:possibilities})
        k+=1
    return bingo_dict

if __name__ == "__main__":
    with open("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d4.txt","r") as f:
        content = f.read().split("\n\n")
        bingo_streak = content[0]
        bingo_cards = [x.split("\n") for x in content[1:]]
    print(solvePart1(bingo_streak.split(","),bingo_cards))
    print(solvePart2(bingo_streak.split(","),bingo_cards))