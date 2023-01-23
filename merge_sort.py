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