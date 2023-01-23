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