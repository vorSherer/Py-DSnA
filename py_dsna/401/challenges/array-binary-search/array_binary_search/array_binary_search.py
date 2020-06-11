def binary_search(lst, key):
    '''
    This function takes in a sorted array and the search key. Without utilizing any of the built-in methods available to python, it returns the index of the array’s element that is equal to the search key, or -1 if the element does not exist.
    '''    
    low, high = 0, len(lst) -1

    while low <= high:
        mid = (low + high) // 2
        if key == lst[mid]:
            return mid
        elif key < lst[mid]:
            high = mid -1
        else:
            low = mid +1
    return -1

