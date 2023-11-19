def search_binary(mylist: list, item: int) -> bool:
    first = 0
    last = len(mylist) - 1
    found_flag = False
    while (first <= last and not found_flag):
        mid = (first + last) // 2
        if mylist[mid] == item:
            found_flag = True
        else:
            if item < mylist[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found_flag


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(search_binary(test_list, 6))
print(search_binary(test_list, 15))
