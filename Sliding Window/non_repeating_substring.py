'''
Given a string, find the length of the longest substring, which has all distinct characters.
'''

def non_repeating_substring(str1): 
    seen = {} 
    windowStart = 0 
    longest = 0 
    
    for windowEnd in range(len(str1)):
        currentChar = str1[windowEnd]
        
        if currentChar not in seen: 
            seen[currentChar] = 0 
        
        seen[currentChar] += 1
        
        while seen[currentChar] > 1: 
            firstChar = str1[windowStart]
            seen[firstChar] -= 1
            
            if seen[firstChar] == 0: 
                del seen[firstChar]
            
            windowStart += 1 
            
        longest = max(longest, windowEnd - windowStart + 1)
        
    return longest

def main():
    print("Length of the longest substring: " +
          str(non_repeating_substring("aabccbb")))
    print("Length of the longest substring: " +
          str(non_repeating_substring("abbbb")))
    print("Length of the longest substring: " +
          str(non_repeating_substring("abccde")))


main()