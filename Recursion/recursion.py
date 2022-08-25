# PS: To run the functions, change the function in the last line of code. 


#Returns numbers in descending order

def descending_num_recurse(num):
    if(num==0):
        return 0
    print(num)
    descending_num_recurse(num-1)

def descending_num():
    num = int(input("Enter upper limit of numbers: "))
    descending_num_recurse(num)


# Factorial using recursion
def factorial_recurse(num):
    if(num==0):
        return 1
    return(factorial_recurse(num-1)*num)

def factorial():
    num = int(input("Enter the number to find factorial of : "))
    print(factorial_recurse(num))

# Sum of first N numbers
def sum_n_recurse(num):
    if(num==0):
        return(0)
    return(num + sum_n_recurse(num-1))

def sum_n():
    num = int(input())
    print(sum_n_recurse(num))

#Fibbonacci numbers
def fibonacci_recurse(num,n):
    if(n==i ):
        return(n)
    print(", %d"%(n),end="")
    n = n+1

def fibonacci():
    num = int(input())
    n=0
    print("0",end="")
    fibonacci_recurse(num,n)

if __name__ == '__main__':
    #descending_num()
    #factorial()
    sum_n()
    