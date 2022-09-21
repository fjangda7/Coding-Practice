'''
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

'''


def pair_with_targetsum(arr, target_sum):
    
    left = 0 
    right = len(arr) - 1
    
    while left < right: 
        currentSum = arr[left] + arr[right]
        if currentSum < target_sum:
            left += 1
        elif currentSum > target_sum:
            right -= 1
        else: 
            return [left, right]
    
def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))


main()