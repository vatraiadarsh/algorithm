def partition(unsorted_array, first_index, last_index):
    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index

    less_then_pivot_index = index_of_last_element
    greater_then_pivot_index = first_index + 1

    while True:
        while unsorted_array[greater_then_pivot_index] < pivot and greater_then_pivot_index < last_index:
            greater_then_pivot_index += 1

        while unsorted_array[less_then_pivot_index] > pivot and less_then_pivot_index >= first_index:
            less_then_pivot_index -= 1

        if greater_then_pivot_index < less_then_pivot_index:
            temp = unsorted_array[greater_then_pivot_index]
            unsorted_array[greater_then_pivot_index] = unsorted_array[less_then_pivot_index]
            unsorted_array[less_then_pivot_index] = temp
        else:
            break

    unsorted_array[pivot_index] = unsorted_array[less_then_pivot_index]
    unsorted_array[less_then_pivot_index] = pivot
    return less_then_pivot_index


def quick_sort(unsorted_array, first, last):
    if last - first <= 0:
        return
    else:
        partition_point = partition(unsorted_array, first, last)
        quick_sort(unsorted_array, first, partition_point-1)
        quick_sort(unsorted_array, partition_point + 1, last)


# [-2, 45, 0, 11, -9]
# here -2 => pivot
# 45 => greater_then_pivot_index
# -9 => less_then_pivot_index


my_list = [-2, 45, 0, 11, -9]
quick_sort(my_list, 0, 4)
print(my_list)


my_list = ['abpple', 'aapple', 'len', 'mon', 'tues', 'cat', 'car']
fst = 0  # starting array from zero
lst = len(my_list)-1
quick_sort(my_list, fst, lst)
print(my_list)
