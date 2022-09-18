'''
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can’t skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.
'''

def fruits_into_baskets(fruits):
    basket = dict() 
    maxFruits = 0
    windowStart = 0 
    
    for windowEnd in range (len(fruits)): 
        currentFruit = fruits[windowEnd]
        
        if currentFruit not in basket: 
            basket[currentFruit] = 0 
            
        basket[currentFruit] += 1
        
        while len(basket) > 2: 
            firstFruit = fruits[windowStart]
            basket[firstFruit] -= 1
            
            if basket[firstFruit] == 0: 
                del basket[firstFruit]
                
            windowStart += 1
        
        maxFruits = max(maxFruits, windowEnd - windowStart + 1)
    
    return maxFruits 
        
def main():
    print("Maximum number of fruits: "
          + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: "
          + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
    