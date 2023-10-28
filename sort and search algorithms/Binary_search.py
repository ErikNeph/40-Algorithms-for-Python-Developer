def search_binary(mylist, item):
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


print(search_binary([1, 2, 3, 4], 11))
