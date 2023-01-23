#Bubble Sort
#Sort the follwoing numbers assigned to you using the Bubble Sort Method

#Assigned Numbers
myNumbers = [24, 6, 7, 88, 51, 40, 11, 68, 79, 5]

#for loop
for i in range(len(myNumbers)-1, 0, -1):
    for j in range(i):
        if myNumbers[j] > myNumbers[j + 1]:

            #swaps the position of the elements
            temp = myNumbers[j]
            myNumbers[j] = myNumbers[j + 1]
            myNumbers[j + 1] = temp

    #displays the breakdown of the bubble sort
    print(myNumbers)

#dislays the final output
print()
print("="*23, "Bubble Sort", "="*24)
print("Using the Bubble Sort Method, the output is: \n", myNumbers)
print("="*60)