def merge_sort(mylist: list) -> list:
    if len(mylist) > 1:
        mid = len(mylist) // 2  # splits list in half
        left = mylist[:mid]
        right = mylist[mid:]

        merge_sort(left)  # repeats until lenght of each list is 1
        merge_sort(right)

        a = 0
        b = 0
        c = 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                mylist[c] = left[a]
                a += 1
            else:
                mylist[c] = right[b]
                b += 1
            c += 1
        while a < len(left):
            mylist[c] = left[a]
            a += 1
            c += 1
        while b < len(right):
            mylist[c] = right[b]
            b += 1
            c += 1
    return mylist


test_list = [23, 10, 15, 20, 8, 4, 53, 41]
print(merge_sort(test_list))
