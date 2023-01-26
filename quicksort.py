#Quicksort
#Sort the following numbers assigned to you using Quicksort Method

# function quicksort
def quicksort(myNumbers, left_side, right_side):
    if left_side < right_side:
        partition_pos = partition(myNumbers, left_side, right_side)
        quicksort(myNumbers, left_side, partition_pos - 1)
        quicksort(myNumbers, partition_pos + 1, right_side)