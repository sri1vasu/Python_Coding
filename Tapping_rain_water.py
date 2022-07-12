# Suppose we have an array of n non-negative integers. These are representing an elevation map where the width of each bar is 1, we have to compute how much water it is able to trap after raining. 

# Define a stack st, water := 0 and i := 0

# left_arr , min of each element comparision iteratively from left
# right_arr , max of each elemnt comparision iteratively from right
# water=0
# water = water + min(left[index],right[index]) - arr[index] 
#Testing Arr=[0,1,0,2,1,0,1,3,2,1,2,1]
#rain_trap(Arr)


def rain_trap(arr):
    size=len(arr)
    water=0
    #two Empty arrays
    left=size*[0]
    right=size*[0]
    
    left[0]=arr[0]
    max_so_far_left=arr[0]
    for index in range(0,size):
        if (max_so_far_left < arr[index]):
            max_so_far_left=arr[index]
            left[index]=max_so_far_left
        else:
            left[index]=max_so_far_left
    max_so_far_right=arr[-1]        
    for index in range(size-1,-1,-1):
        if (max_so_far_right < arr[index]):
            max_so_far_right=arr[index]
            right[index]=max_so_far_right
        else:
            right[index]=max_so_far_right     
            
    for index in range(0,size):
        water+= min(left[index],right[index]) -arr[index]
    return water
        
            
