#Quicksort
#Sort the following numbers assigned to you using Quicksort Method

# function quicksort
def quicksort(myNumbers, left_side, right_side):
    if left_side < right_side:
        partition_pos = partition(myNumbers, left_side, right_side)
        quicksort(myNumbers, left_side, partition_pos - 1)
        quicksort(myNumbers, partition_pos + 1, right_side)

# function partition
def partition(myNumbers, left_side, right_side):
    i = left_side
    j = right_side - 1
    pivot = myNumbers[right_side]

    # while loop
    while i < j: 
        while i < right_side and myNumbers[i] < pivot:
            i += 1

        while j > left_side and myNumbers[j] >= pivot:
            j -= 1

        if i < j:
            temp = myNumbers[i]
            myNumbers[i] = myNumbers[j]
            myNumbers[j] = temp 

    if myNumbers[i] > pivot:
        temp = myNumbers[i]
        myNumbers[i] = myNumbers[right_side]
        myNumbers[right_side] = temp

    #displays the breakdown of the quicksort method
    print(myNumbers)
    return i

myNumbers = [24, 6, 7, 88, 51, 40, 11, 68, 79, 5]
quicksort(myNumbers, 0, len(myNumbers) - 1)