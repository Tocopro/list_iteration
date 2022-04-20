# iteration simultaneously

def iteration_list():
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 0]

    for x, y in zip(list1, list2[::-1]):
        print(x, y)


iteration_list()

