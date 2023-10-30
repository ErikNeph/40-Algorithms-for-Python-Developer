def intpol_search(mylist: list, item: int) -> bool:
    idx_0 = 0
    idxn = len(mylist) - 1
    found = False
    while idx_0 < idxn and item >= mylist[idx_0] and item <= mylist[idxn]:
        # Looking for the middle point
        middle = idx_0 + int(
            (
                (float(idxn - idx_0) / (mylist[idxn] - mylist[idx_0]))
                * (item - mylist[idx_0])
            )
        )
        # Compare the value at the midpoint with the search value
        if mylist[middle] == item:
            found = True
            return found
        if mylist[middle] < item:
            idx_0 = middle + 1
    return found


test_list = [10, 11, 12, 13, 14, 15, 16, 17, 18]
print(intpol_search(test_list, 11))
print(intpol_search(test_list, 20))
