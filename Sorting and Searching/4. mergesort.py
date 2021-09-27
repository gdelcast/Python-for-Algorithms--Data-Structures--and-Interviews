
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    arr1 = merge_sort(arr[:len(arr)//2])                    # split array 1st half (recursive)
    arr2 = merge_sort(arr[len(arr)//2:])                    # split array 2nd half (recursive)

    if len(arr1)==1 and len(arr2)==1 and arr2[0]<arr1[0]:   # checks last 2 elements and return swap
        return arr2 + arr1
    elif arr2[0]>arr1[0]:
        return arr                                          # if correct order return 2 elements as is
    else:
        temp = []
        while arr1 and arr2:                                # received 2 sorted arrays, parse 1st ele of each and add to temp
            if arr1[0]<arr2[0]:
                temp.append(arr1[0])
                del arr1[0]
            else:
                temp.append(arr2[0])
                del arr2[0]
        return temp + arr1 + arr2                           # return temp + remaining elements in arr1 and arr2
                                                            # (if sorted 1 of the arrays will have several ele after comparison)


arr = [5,3,4,6,8,1,2,12,41,25]
print(merge_sort(arr))