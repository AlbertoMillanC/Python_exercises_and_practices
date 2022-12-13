def find_max(nums):
    max_num = float("-inf" )  # smaller than all other numbers
    for num in nums:
        if num > max_num:
           max_num +=1
    return max_num

for find_max in range(10):
    print (find_max)

