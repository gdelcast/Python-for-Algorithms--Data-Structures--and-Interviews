import random
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    pivot = 0                                   # picks a random pivot (first element)

    i = len(arr)-1 
    while i > pivot:                            # parse all elements before 
        
        temp = arr[i]

        if arr[i]< arr[pivot]:                  # if pos is less swaps with pivot +1 and shift the array up
            arr[i] = arr[pivot+1]
            arr[pivot+1] = arr[pivot]
            arr[pivot] = temp
            pivot = pivot+1
        #else:                                  # if not, checks next pos
        i -= 1
    
    
    return  quick_sort(arr[:pivot]) + [arr[pivot]] +  quick_sort(arr[pivot+1:])       #merge sub array + sorted array after pivot

arr = [5,3,4,6,8,1,2,12,41,25]
print(quick_sort(arr))