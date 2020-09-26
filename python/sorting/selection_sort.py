def selection_sort(unsorted_list):
    size_of_list = len(unsorted_list)
    for i in range(size_of_list):
        for j in range(i+1, size_of_list):
            if unsorted_list[j] < unsorted_list[i]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[j]
                unsorted_list[j] = temp


my_list = [-2, 45, 0, 11, -9]
selection_sort(my_list)
print(my_list)

my_list = ['abpple', 'aapple', 'len', 'mon', 'tues', 'cat', 'car']
selection_sort(my_list)
print(my_list)
