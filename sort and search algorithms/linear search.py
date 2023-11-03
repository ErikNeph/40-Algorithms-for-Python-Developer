def linear_search(mylist: list, item: int) -> bool:
    index = 0
    found = False
    
    # Compare the value with each data element
    while index < len(mylist) and found is False:
        if mylist[index] == item:
            found = True
        else:
            index += 1
    return found


test_list = [12, 22, 33, 9, 40, 25, 77]
print(linear_search(test_list, 33))
print(linear_search(test_list, 55))
