choice = input("do you wish to start, if no give no else PRESS ENTER """) #Letting the user choose if he/she wants to start or not
                                                                          #if they choose no the code does not start
while choice != "no": # starting a while loop if they want                     
    function = input("give the function """).lower() # let the user give a function

    if function == "multiply": # if the function is given multiply this will run
        num1 = int(input("give a number to multiply """))  
                                                              # letting the user choose the numbers
        num2 = int(input("give a number to multiply with first number """))

        print(num1*num2)# printing the multiplication result
        
    elif function == "addition": # if the function is given addition this will run
        num_1 = int(input("give a number to add """))
        num_2 = int(input("give a number to add with first number """))
        print(num_1+num_2)   

    elif function == "subtraction": # if the function is given subtraction this will run

        num3 = int(input("give number to substract """))# letting the user choose the numbers
        num4 = int(input("give a number to substract from the first number """))
        print(num3 - num4)

    elif function == "division": # if the function is given division this will run

        num5 = int(input("give a  dividend """)) # letting the user choose the numbers
        num6 = int(input("give the divisor """))
        print("The quotient is" ,num5/num6 )

    elif function == "exit": # if the function is given exit then the code will break
        break
    
    else:
        print("no function given") # if the function is given nothing it will print this
