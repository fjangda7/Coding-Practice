'''
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
'''

def length_of_longest_substring(arr, k):
    zeroCount = 0 
    longest = 0 
    windowStart = 0
    
    for windowEnd in range(len(arr)): 
        
        if arr[windowEnd] == 0: 
            zeroCount += 1
            
        while zeroCount > k: 
            if arr[windowStart] == 0: 
                zeroCount -= 1
            windowStart += 1
            
        longest = max(longest, windowEnd - windowStart + 1)
        
    return longest

def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()