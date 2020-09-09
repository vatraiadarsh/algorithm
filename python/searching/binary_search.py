def binary_search_iterative(ordered_list, term):
    size_of_list = len(ordered_list)-1
    index_of_first_element = 0
    index_of_last_element = size_of_list

    while index_of_first_element <= index_of_last_element:
        mid_point = (index_of_first_element + index_of_last_element)//2
        if ordered_list[mid_point] == term:
            return mid_point
        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1

        if index_of_first_element > index_of_last_element:
            return None


"""
The implementation we discussed above is an iterative one. 
We can also develop a recursive variant of the algorithm by applying the same principle and shifting the pointers
that mark the beginning and end of the search list.
"""


store = [2, 4, 5, 12, 43, 54, 60, 77]
a = binary_search_iterative(store, 60)
print("Index position of value 2 is ", a)


def binary_search_recursive(ordered_list, first_element_index, last_element_index, term):
    if(last_element_index < first_element_index):
        return None
    else:
        mid_point = first_element_index + \
            ((last_element_index - first_element_index)//2)

    if ordered_list[mid_point] > term:
        return binary_search_recursive(ordered_list, first_element_index, mid_point-1, term)
    elif ordered_list[mid_point] < term:
        return binary_search_recursive(ordered_list, mid_point+1, last_element_index, term)
    else:
        return mid_point


store = [2, 4, 5, 12, 43, 54, 60, 77]
a = binary_search_recursive(store, 0, len(store), 67)
print("Index position of value 67 is ", a)
