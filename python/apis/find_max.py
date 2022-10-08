#funcion para encotrar un numero maximo de una lista

def find_max(nums):
        max_num = float("-inf")
       
        # smaller than all other numbers
        for i in nums:
                if i > max_num:
                        max_num = i                                  # (Fill in the missing line here)
        return max_num
nums = [2,10,7,4,6]
__name__ == "__main__"  
find_max(nums)
# num = max_num
# max_num += 1
# max_num = num
# max_num += num