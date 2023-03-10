#Selection Method
#Sort the following numbers assigned to you

#Assigned numbers
myNumbers = [24, 6, 7, 88, 51, 40, 11, 68, 79, 5]

#for loop
for i in range(len(myNumbers)):
    min_index = i #let i be the smallest number in the array
    for j in range(i + 1, len(myNumbers)):
        if myNumbers[j] < myNumbers[min_index]:
            min_index = j 

    #swap the element in ascending order
    temp = myNumbers[i]
    myNumbers[i] = myNumbers[min_index]
    myNumbers[min_index] = temp

    #displays the breakdown of the selection sort
    print(myNumbers)

#displays the output
print()
print("="*22, "Selection Sort", "="*22)
print("Using the Selection Sort Method, the output is: \n", myNumbers)
print("="*60)