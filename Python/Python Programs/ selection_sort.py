import sys

def selection_sort(arr):
    # This function will sort the array in non-decreasing order. 
    n = len(arr)
    #The outer loop will run for n times.
    for i in range(n):
        min_index = i
        # The inner loop will run for n-i-1 times as the
        # first i elements are already in sorted.
        for j in range(i+1, n):
        # Compare if the present element is smaller than the
        #  element present at min_index in the array. If yes
        # store the index of the present element in min-index.
            if arr[min_index] > arr[j]:
                min_index = j
        # Swap the ith element with the smallest element in the
        # unsorted list i.e. arr[min_index}].
        if i != min_index:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp 
    return arr
    
# main code
if __name__=='__main__':

    arr = [21, 15, 96, 37, 72, 54, 68, 41, 85, 30]
    print("Sorted array: ")
    print(selection_sort(arr))
