def reach_point(i):
    i+=1
    if i < 50:
        reach_point(i)

    return 'hi'

if __name__ == '__main__':
    print(reach_point([9,7,4]))