#Insertion Sort
#Sort the following numbers assigned to you using Insertion Sort

#Assigned numbers
myNumbers = [24, 6, 7, 88, 51, 40, 11, 68, 79, 5]

#for loop
for i in range(1, len(myNumbers)):
    j = i 

    #while loop
    while myNumbers[j - 1] > myNumbers[j] and j > 0:
        temp = myNumbers[j - 1]
        myNumbers[j - 1] = myNumbers[j]
        myNumbers[j] = temp
        j -= 1

    #displays the breakdown of the insertion sort
    print(myNumbers)