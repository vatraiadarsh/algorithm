#  we split the list into two approximate halves.
#  We continue to divide the list into two halves recursively.
#  The sublists are created as a result of the recursive call will contain only one element.
#  At that point, we begin to merge the solutions in the conquer or merge step:

def merge_sort(unsorted_array):
    if len(unsorted_array) == 1:
        return unsorted_array

    mid_point = int(len(unsorted_array)//2)
    # [first_half:mid_point:second_half]
    first_half = unsorted_array[:mid_point]
    second_half = unsorted_array[mid_point:]

    half_a = merge_sort(first_half)
    half_b = merge_sort(second_half)

    return merge(half_a, half_b)


def merge(first_sublist, second_sublist):
    i = j = 0
    # pointers to tell us where we are in the two lists with respect to the merging process.
    merged_list = []
    while i < len(first_sublist) and j < len(second_sublist):
        if first_sublist[i] < second_sublist[j]:
            merged_list.append(first_sublist[i])
            i += 1
        else:
            merged_list.append(second_sublist[j])
            j += 1

    while i < len(first_sublist):
        merged_list.append(first_sublist[i])
        i += 1

    while j < len(second_sublist):
        merged_list.append(second_sublist[j])
        j += 1

    # There may be elements left behind in either first_sublist or second_sublist.
    # These last two while loops make sure that those elements are added to merged_list before it is returned.

    return merged_list


my_list = [4, 3, 2, 1]
print(merge_sort(my_list))

my_list = ['abpple', 'aapple', 'len', 'mon', 'tues', 'cat', 'car']
print(merge_sort(my_list))
