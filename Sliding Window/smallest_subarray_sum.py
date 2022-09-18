'''
Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
'''
import math 

def smallest_subarray_sum(s, arr):
    
    currentSum = 0
    windowStart = 0 
    windowLength = 0 
    smallestLength = math.inf
    
    for windowEnd in range(len(arr)): 
        currentSum += arr[windowEnd]
        windowLength += 1
        
        while currentSum >= s: 
            smallestLength = min(smallestLength, windowLength)
            currentSum -= arr[windowStart]
            windowLength -= 1
            windowStart += 1
            
    return smallestLength

def main():
    print("Smallest subarray length: "
          + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: "
          + str(smallest_subarray_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: "
          + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))


main()
    