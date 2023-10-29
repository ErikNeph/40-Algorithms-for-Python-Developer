def insertion_sort(mylist: list) -> list:
    for i in range(1, len(mylist)):
        j = i - 1
        element_next = mylist[i]
        while (mylist[j] > element_next) and (j >= 0):
            mylist[j + 1] = mylist[j]
            j = j - 1
        mylist[j + 1] = element_next
    return mylist


print(insertion_sort([1, 3, 2, 5, 6, 4]))
