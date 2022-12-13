#funcion para encotrar un numero maximo de una lista

def find_max(nums):
        max_num = float("-inf")
        for i in nums:
                if i > max_num:
                        max_num = i                                 
        return max_num

nums = 2.8,3.53,4.5,78.8,12.8,1.8,2.7,555.5

__name__ == "__main__"  
find_max(nums)