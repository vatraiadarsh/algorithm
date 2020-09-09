"""
The interpolation searching algorithm, the improved version of the binary search algorithm.

mid_point = lower_bound_index + (( upper_bound_index - lower_bound_index)// (input_list[upper_bound_index] - input_list[lower_bound_index])) * (search_value - input_list[lower_bound_index]) 

The lower_bound_index variable is the lower-bound index, which is the index of the smallest value in the, upper_bound_index list, 
denoting the index position of the highest value in the list. The input_list[lower_bound_index]  and input_list[lower_bound_index]
variables are the lowest and highest values respectively in the list. The search_term variable contains the value of 
the item that is to be searched.
"""


def nearest_mid(input_list, lower_bound_index, upper_bound_index, search_value):
    return lower_bound_index + ((upper_bound_index - lower_bound_index) // (input_list[upper_bound_index] - input_list[lower_bound_index])) * (search_value - input_list[lower_bound_index])


'''
The nearest_mid function takes, as arguments, the lists on which to perform the search. 
The lower_bound_index and upper_bound_index parameters represent the bounds in the list 
within which we are hoping to find the search term. Furthermore, search_value represents the value being searched for.

Given our search list, 44, 60, 75, 100, 120, 230, and 250, nearest_mid will be computed with the following values:

lower_bound_index = 0
upper_bound_index = 6
input_list[upper_bound_index] = 250
input_list[lower_bound_index] = 44
search_value = 230

Lets compute the mid_point value:

mid_point= 0 + [(6-0)//(250-44) * (230-44)
         = 5 
'''


def interpolation_search(ordered_list, term):
    size_of_list = len(ordered_list)-1
    index_of_first_element = 0
    index_of_last_element = size_of_list

    while index_of_first_element <= index_of_last_element:
        mid_point = nearest_mid(
            ordered_list, index_of_first_element, index_of_last_element, term)

        if mid_point > index_of_last_element or mid_point < index_of_first_element:
            return None

        if ordered_list[mid_point] == term:
            return mid_point

        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else:
            index_of_first_element = mid_point - 1

    if index_of_first_element > index_of_last_element:
        return None


store = [2, 4, 5, 12, 43, 54, 60, 77]
a = interpolation_search(store, 60)
print("Index position of value 2 is ", a)
