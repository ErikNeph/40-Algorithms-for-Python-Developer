def shell_sort(mylist: list) -> list:
    distance = len(mylist) // 2
    while distance > 0:
        for i in range(distance, len(mylist)):
            temp = mylist[i]
            j = i
            # sort the sublist by the current distance value
            while j >= distance and mylist[j - distance] > temp:
                mylist[j] = mylist[j - distance]
                j -= distance

            mylist[j] = temp
        # reducing the distance to the next element
        distance = distance // 2

    return mylist


test_list = [25, 4, 11, 54, 57, 22, 10, 67, 2, 45]
print(shell_sort(test_list))
