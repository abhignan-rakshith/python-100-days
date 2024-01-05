#Bubble sort in python

def bubbleSort(arr):
    """This function executes bubble sort algorithm"""
    array_len = len(arr)
    switch = False
    
    for i in range(array_len - 1):
        for j in range(0, array_len-i-1):
            if arr[j] > arr[j + 1]:
                switch = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
            if not switch:
                return
    

my_arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(my_arr)

print("The sorted array is:\t")
for i in range(len(my_arr)):
    print("%d"%my_arr[i], end = " ")