# last_ele_index = len(list) - 1
# print(0, list)
# for idx in range(last_ele_index):
#     if list[idx] > list[idx + 1]:
#         list[idx], list[idx + 1] = list[idx + 1], list[idx]
#     print(idx + 1, list)


def bubble_sort(mylist: list) -> list:
    # Excahnge the elements to arrange in order
    prelast_elem_index = len(mylist) - 1
    for pass_no in range(prelast_elem_index, 0, -1):
        for idx in range(pass_no):
            if mylist[idx] > mylist[idx + 1]:
                mylist[idx], mylist[idx + 1] = mylist[idx + 1], mylist[idx]
    return mylist


print(bubble_sort([25, 21, 22, 24, 23, 27, 26]))
