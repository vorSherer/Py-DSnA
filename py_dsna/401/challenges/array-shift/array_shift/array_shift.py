def insert_shift_array(lst, value):
    for i in range(0, len(lst)-1):
        idx = len(lst) // 2
        if lst[i] == idx:
            lst.append(value)
        return lst
