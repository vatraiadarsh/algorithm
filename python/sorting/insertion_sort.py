# def insertion_sort(unsorted_list):
#     for index in range(1, len(unsorted_list)):
#         search_index = index
#         insert_value = unsorted_list[index]
#         while search_index > 0 and unsorted_list[search_index-1] > insert_value:
#             unsorted_list[search_index] = unsorted_list[search_index-1]
#             search_index -= 1
#         unsorted_list[search_index] = insert_value


# my_list = [10, 11, 12, 1, 2, 3]
# print(my_list)
# insertion_sort(my_list)
# print(my_list)


def insertion_sort(unsorted_list):
    for i in range(1, len(unsorted_list)):
        value_to_sort = unsorted_list[i]

        while i > 0 and unsorted_list[i - 1] > value_to_sort:
            unsorted_list[i] = unsorted_list[i-1]
            i -= 1

        unsorted_list[i] = value_to_sort


my_list = [4, 3, 2, 1]
insertion_sort(my_list)
print(my_list)

my_list = ['abpple', 'aapple', 'len', 'mon', 'tues', 'cat', 'car']
insertion_sort(my_list)
print(my_list)
