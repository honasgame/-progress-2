def getSum(n): # Creating a function where n is the input given by the user
 
    sum = 0 # Storing 0 in sum variable

    while (n != 0): # starting a while loop until n is not equal to 0
 
        sum = sum + n % 10 # iterating over the value of sum by adding sum to the remainder of n and 10 and again storing it in sum

        n = n//10 # dividing n and 10 and storing the answer (which will be a whole number by the use of // operator)  in n
 
    return sum # returning the value of sum when n becomes 0
 
 

n = int(input("Enter any number:\n")) # letting the user give the input and converting it to integer
print(getSum(n)) # printing the function