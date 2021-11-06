def merge_sort(num):
    if not num: return []
    if len(num)<2:  return num
    
    n = len(num)//2
    left = merge_sort(num[:n])
    right = merge_sort(num[n:])

    out =[]
    while left and right:
        if left[0] < right[0]:
            out.append(left.pop(0))
        else:
            out.append(right.pop(0))
    
    return out + left + right

    
            
arr =[5,3,4,6,8,1,2,12,41,25]
print(merge_sort(arr))