num = input("give some numbers") # input given by the user will be stored in num 

sum_digits = 0 # storing 0 in a variable

for digit in str(num): # calling a loop to loop over num while making num a string

    sum_digits += int(digit) # looping sum_of_digits adding to digits in num
    # and storing the value in again in sum_of_digits 
    # until the last digit while making each digit a integer from string
                                
print(sum_digits) # printing the value stored in sum_digits