def find_max(nums):
    max_num = float("-inf") #Menor que todos os outros números
    for num in nums:
        if num in nums:
            if num > max_num:
                #max_num+=1
                #num = max_num
                #max_num = num
                #max_num += num
                #Try any of the opetions above
    return max_num