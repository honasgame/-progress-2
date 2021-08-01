num = int(input("give number"))
x = int(input("give from"))
y = int(input("give to"))
y_2 = y + 1
for i in range(x,y_2):
    print(num , "x" , i , "=" , num*i)