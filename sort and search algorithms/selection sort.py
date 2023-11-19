def selection_sort(mylist: list) -> list:
    for fill_slot in range(len(mylist) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if mylist[location] > mylist[max_index]:
                max_index = location

        mylist[fill_slot], mylist[max_index] = mylist[max_index], mylist[fill_slot]

    return mylist


test_list = [40, 22, 1, 2, 3, 67, 33, 15]
print(selection_sort(test_list))
