#############
# Задание 4 #
#############

nums = input("Введите путь к файлу")

#with open('nums.txt', 'r') as file:
    #nums = [line.strip() for line in file]
 
nums = [1, 2, 3, 4]

def minMoves(nums) -> int:
   total_sum = sum(nums)
   min_value = min(nums)
   moves = total_sum - min_value * len(nums)
   return moves
  
print(minMoves( nums))  
