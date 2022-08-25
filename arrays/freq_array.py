
def freqArray():
    counter = [0]*10
    for i in arr:
        counter[i] += 1
    print(counter)

arr = [2,3,4,5,6,7,8,2,3,4,5,6,7,8]

freqArray()