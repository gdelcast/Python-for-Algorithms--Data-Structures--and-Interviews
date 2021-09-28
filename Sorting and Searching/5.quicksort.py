import random
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    pivot = len(arr)-1                          # picks a random pivot (last element)
    #pivot = random.randint(0,len(arr)-1)
    #pivot = len(arr)//2

    i = 0 
    while i < pivot:                            # parse all elements before 
        
        temp = arr[i]

        if arr[i]> arr[pivot]:                  # if pos is greater swaps with pivot -1 and shift the array down
            arr[i] = arr[pivot-1]
            arr[pivot-1] = arr[pivot]
            arr[pivot] = temp
            pivot -= 1
        else:                                  # if not, checks next pos
            i += 1
    

    return quick_sort(arr[:pivot]) + [arr[pivot]] +  quick_sort(arr[pivot+1:])       #merge sub array + sorted array after pivot

arr = [5,3,4,6,8,1,2,12,41,25]
print(quick_sort(arr))