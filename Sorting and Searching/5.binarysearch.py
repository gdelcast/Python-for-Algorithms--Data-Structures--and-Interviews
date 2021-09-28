# array needs to be ordered

def binary_search(arr,ele):
    if len(arr)<1:
        return None
    
    if len(arr)==1 and arr[0]==ele:
        return True
    elif len(arr)==1 and arr[0]!=ele:
        return False
    else:
        middle = (len(arr)-1)//2
        if ele<arr[middle]:
            return binary_search(arr[:middle],ele)
        else:
            return binary_search(arr[middle:],ele)



arr = [1, 2, 5, 3, 4, 6, 8, 12, 25, 41]
print(binary_search(arr,12))
