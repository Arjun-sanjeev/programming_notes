num_rows = int(input("Enter number of rows: "))

print("\n\n")

for rows in range(1,num_rows+1):
    for num in range(1,rows+1):
        print(num,end=" ")
    
    for blanks in range((num_rows-rows)*2):
        print("*",end=" ")
    
    for num in range(rows,0,-1):
        print(num,end=" ")

    print()

print("\n\n")

'''
Output

1 * * * * * * * * 1 
1 2 * * * * * * 2 1 
1 2 3 * * * * 3 2 1 
1 2 3 4 * * 4 3 2 1 
1 2 3 4 5 5 4 3 2 1 

'''