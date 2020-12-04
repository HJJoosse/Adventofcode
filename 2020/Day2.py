import re
with open("input_d2","r") as f:
    content = f.read()

parser = (x for x in re.split('\n',content))

passwords = []
for pars_item in parser:
    try:
        passwords.append((re.split(':\W',pars_item)[0],re.split(':\W',pars_item)[1]))
    except IndexError:
        continue

good_passes = 0
for rule,password in passwords:
    split_key= re.split('\W|-',rule)
    min_am= int(split_key[0])
    max_am= int(split_key[1])
    letter = split_key[2]
    if ((password[min_am-1] == letter) & (password[max_am-1] != letter)) or\
            ((password[min_am-1] != letter) & (password[max_am-1] == letter)) :

        good_passes+=1
    else:
        continue

print(good_passes)
