def insert_shift_array(lst, value):
    '''
    This function takes in an array and the value to be added. Without utilizing any of the built-in methods available to python, it returns an array with the new value added at the middle index.
    '''

    for i in range(0, len(lst)-1):
        idx = (len(lst)+1) // 2
        lst = lst[:idx] + [value] + lst[idx:]
        return lst

