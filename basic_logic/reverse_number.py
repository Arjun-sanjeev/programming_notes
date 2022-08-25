num = input("Enter number to be reversed: ")

#Python way
# num = num[::-1]
# print(num)

num = int(num)
rev = 0
while(num>0):
    rev = 10*rev
    rev += num%10
    num = num//10

print(rev)