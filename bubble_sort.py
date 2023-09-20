# BUBBLE SORT


def bubble_sort(my_list):
    unsorted_last_index = len(my_list) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(unsorted_last_index):
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                sorted = False
        unsorted_last_index -= 1
    return my_list

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted array is:", my_list)