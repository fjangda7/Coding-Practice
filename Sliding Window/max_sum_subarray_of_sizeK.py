
'''
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
'''

def maxSum(arr, k):
    maxSum, currentSum = 0, 0
    windowStart = 0 
    
    for windowEnd in range(len(arr)): 
        currentSum += arr[windowEnd]
        
        #is the sliding window of size k?
        if windowEnd >= (k-1): 
            maxSum = max(maxSum, currentSum)
            currentSum -= arr[windowStart]
            windowStart += 1
            
    return maxSum

def main():
    print("Maximum sum of a subarray of size K: " +
          str(maxSum([2, 1, 5, 1, 3, 2], 3)))
    print("Maximum sum of a subarray of size K: " +
          str(maxSum([2, 3, 4, 1, 5], 2)))


main()