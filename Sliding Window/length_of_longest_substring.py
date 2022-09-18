'''
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.
'''

def length_of_longest_substring(str1, k):
    longest = 0
    seen = dict() 
    windowStart = 0 
    sameLetterMax = 0
    
    for windowEnd in range(len(str1)): 
        
        currentChar = str1[windowEnd]
        if currentChar not in seen: 
            seen[currentChar] = 0 
        seen[currentChar] += 1
        
        sameLetterMax = max(sameLetterMax, seen[currentChar])
        
        if (windowEnd - windowStart + 1 - sameLetterMax) > k: 
            firstChar = str1[windowStart]
            seen[firstChar] -= 1
            
            if seen[firstChar] == 0:
                del seen[firstChar]
            
            windowStart += 1
        
        longest = max(longest, windowEnd - windowStart + 1)
        
    return longest 

def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()