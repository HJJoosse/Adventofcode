def split_index(content,batchsize):
    return content[:batchsize], content[batchsize:]

with open('2019/inputs/input_d8','r') as f:
    content = [int(x) for x in f.read()]

batchsize = 25*6
amount_zeroes = batchsize
colours = [2]*batchsize

while len(content) != 0:
    layer, content = split_index(content,batchsize)
    if layer.count(0) < amount_zeroes:
        amount_zeroes = layer.count(0)
        total_sum = layer.count(1)*layer.count(2)  
    colours = [layer[i] if (layer[i]!= 2) & (colours[i] == 2) else colours[i] for i in range(batchsize)]

colours = ["".join(map (str, colours))[(i-1)*25:(25*i)] for i in range(1,7)]

print(f'part 1 = {total_sum}')
for line in colours:
    print(line)
