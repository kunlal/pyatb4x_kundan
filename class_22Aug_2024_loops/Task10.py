#Factorial

number = int(input("Please enter a number!"))
p = 1
for i in range(number,1,-1):
    p = i * p
print("Factorial",p)
