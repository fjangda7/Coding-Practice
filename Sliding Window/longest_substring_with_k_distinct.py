'''
Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.

'''

def longest_substring_with_k_distinct(str1, k):
    numOfDistinct = 0
    windowStart = 0 
    longest = 0
    seen = dict()
    
    for windowEnd in range(len(str1)): 
        currentChar = str1[windowEnd]
        
        if currentChar not in seen: 
            seen[currentChar] = 0
        seen[currentChar] += 1
        
        while len(seen) > k: 
            firstChar = str1[windowStart]
            seen[firstChar] -= 1
            if seen[firstChar] == 0: 
                del seen[firstChar]
            windowStart += 1
        
        
        longest = max(longest, windowEnd - windowStart + 1)
    
    return longest 

def main():
    print("Length of the longest substring: "
          + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: "
          + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: "
          + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()

        