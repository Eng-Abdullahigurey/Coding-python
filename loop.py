num= int(input("Enter a number:"))
total= 0
for i in range(1 , num + 1):
    total +=i
    print("Sum is ", total)
    #Write the file:
    with open("sum.txt" , "w") as file:
        file.write("The sum of numbers from 1 to " + str(num) + " is:" + str(total) + "\n")
        #Opotional: Also print to console:
        print("The sum of numbers from 1 to " , num , "is:" , total)
        