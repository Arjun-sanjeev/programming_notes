from audioop import reverse


def reverseArr(start,end):
    while(start<end):
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    
def rightRotate(length, num_rotations):
    reverseArr(length-num_rotations,length-1)
    reverseArr(0,length-num_rotations-1)
    reverseArr(0,length-1)

def leftRotate(length, num_rotations):
    reverseArr(0,num_rotations-1)
    reverseArr(num_rotations,length-1)
    reverseArr(0,length-1)

arr = [1,2,3,4,5]

rightRotate(5,2)
print(arr)

arr = [1,2,3,4,5]

leftRotate(5,2)
print(arr)