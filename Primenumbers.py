list = [0,1,2, 3, 4, 5, 6, 7]


def is_part_of_series(lst):
    for x in lst:
        if x==0:
            a=0
            print(a)
        elif x==1:
            b=1
            print(b)

        else:
            n = 2 * (x - 1) - 2 * (x - 2)
    print(n)


is_part_of_series(list)




