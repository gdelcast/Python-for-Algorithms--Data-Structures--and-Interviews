def merge_sort(num):
    if not num: return []
    if len(num)<2:  return num
    
    n = len(num)//2
    left = merge_sort(num[:n])
    right = merge_sort(num[n:])
    return merge(left, right)

def merge(left, right):
    if not left or not right : return
    
    out = []
    l = r = 0
    
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            out.append(left[l])
            l +=1
        else:
            out.append(right[r])
            r +=1
    
    out += left[l:]
    out += right[r:]
    return out

    
            
arr =[5,3,4,6,8,1,2,12,41,25]
print(merge_sort(arr))