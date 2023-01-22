def quicksort(nums):
    
    nums_len = len(nums)
    
    if nums_len == 0:
        return []
    
    elif nums_len == 1:
        return nums
    
    else:
        
        pivot = nums[0]
        
        smaller = []
        bigger = []
        pivot_list = []
        pivot_list.append(pivot)
    
        i = 1
        
        while i < nums_len:
 
            if nums[i] < pivot:
                smaller.append(nums[i])
            else:
                bigger.append(nums[i])
            
            i += 1
    
    return(quicksort(smaller) + pivot_list + quicksort(bigger))
    

