#Merge Sort
#Sort the following numbers assigned to you using Merge Sort

#define a function
def merge_sort(myArray):
    if len(myArray) > 1:
        middle = len(myArray)//2
        left_side = myArray[:middle]
        right_side = myArray[middle:]
    
        #recursive iteration
        merge_sort(left_side)
        merge_sort(right_side)

        #merge
        i = 0 # this is for the left side array index
        j = 0 # this is for the right side array index
        k = 0 # this is for the merged array index

        # first while loop
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                myArray[k] = left_side[i]
                i += 1
            else:
                myArray[k] = right_side[j]
                j += 1
            k += 1

        # second while loop
        while i < len(left_side):
            myArray[k] = left_side[i]
            i += 1
            k += 1

        # third while loop
        while j < len(right_side):
            myArray[k] = right_side[j]
            j += 1
            k += 1

    # display the breakdown of the merge sort
    print(myArray)

# calls the function
myNumbers = [24, 6, 7, 88, 51, 40, 11, 68, 79, 5]
merge_sort(myNumbers)

# displays the final output
print()
print("="*24, "Merge Sort", "="*24)
print("Using the Merge Sort Method, the output is: \n", myNumbers)
print("="*60)