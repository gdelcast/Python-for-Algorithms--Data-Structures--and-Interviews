from collections import deque
def quicksort_recursive(arr):   # O (nlogn) time - O(n) space recursive
    if not arr: return []
    pivot = len(arr)-1
    i=0
    while i<pivot:
        if arr[i]>arr[pivot]:
            temp = arr[i]
            arr[i] = arr[pivot-1]
            arr[pivot-1] = arr[pivot]
            arr[pivot] = temp
            pivot-=1
        else:
            i +=1
    return quicksort_recursive(arr[:pivot]) + [arr[pivot]] + quicksort_recursive(arr[pivot+1:])

def mergesort_recursive(arr):   # O (nlogn) time - O(n) space
    if len(arr)>1:

        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergesort_recursive(left)
        mergesort_recursive(right)

        i = j = k = 0

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1

        while i<len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k] = right[j]
            j+=1
            k+=1

def mergesort_recursive2(arr):  # O(nlogn) time - O(n) space
    if len(arr)<=1:
        return arr
    left = deque(mergesort_recursive2(arr[:len(arr)//2]))
    right = deque(mergesort_recursive2(arr[len(arr)//2:]))
    temp = []
    while left and right:
        if left[0]<right[0]:
            temp.append(left.popleft())
        else:
            temp.append(right.popleft())
    return temp + list(left) + list(right)

        
        

arr = [2,4,5,8,9,0,112,3,7,10]
#print(quicksort_recursive(arr))
#mergesort_recursive(arr)
#print(arr)
print(mergesort_recursive2(arr))