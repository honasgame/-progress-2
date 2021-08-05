x = int(input("enter a number"))
y = int(input("enter another number"))
for num in range(x,y):
    if num % 2 == 0:
        print(num, "is an even number")
    elif num % 2 != 0:
        print(num,"is an odd number")
    