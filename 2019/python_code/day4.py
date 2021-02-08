from collections import Counter

start_point = 172851
end_point = 675869

def is_double(digit:str):
    a = int(digit[0])
    for b in digit[1:]:
        if a == int(b):
            return True
        else:
            a = int(b)
    return False

def is_double_correctly(digit:str):
    ct = Counter(digit)
    if 2 in ct.values():
        return True
    else:
        return False
    
def is_incrementing(digit:str):
    if "".join(sorted(digit)) == digit:
        return True
    else:
        return False

def find_passwords(start_point:int = start_point,end_point:int = end_point):
    passwords = []
    for i in range(start_point,end_point+1):
        if is_incrementing(str(i)):
            if is_double(str(i)):
                passwords.append(i)
    return passwords

def find_correct_passwords(start_point:int = start_point,end_point:int = end_point):
    passwords = []
    for i in range(start_point,end_point+1):
        if is_incrementing(str(i)):
            if is_double_correctly(str(i)):
                passwords.append(i)
    return passwords

if __name__ == "__main__":
    print(len(set(find_passwords())))
    print(len(set(find_correct_passwords())))