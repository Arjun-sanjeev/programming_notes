
num_inputs = int(input("Enter number of numbers to find first digit of: "))

for _ in range(num_inputs):
    number = int(input("Enter number to find first digit of: "))
    while(number>0):
        rem = number%10
        number = number//10
    print(rem)


#this does not work for -ve numbers
