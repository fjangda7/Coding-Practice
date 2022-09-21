'''
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

'''
def make_squares(arr):
    
    squares = [0 for x in range(len(arr))]
    highestIndex = len(arr) - 1
    
    left, right = 0, len(arr) - 1
    
    while (left <= right): 
        leftSquare, rightSquare = arr[left] ** 2 , arr[right] ** 2 
        if leftSquare > rightSquare: 
            squares[highestIndex] = leftSquare
            left += 1
        else: 
            squares[highestIndex] = rightSquare
            right -= 1
        
        highestIndex -= 1
    
    return squares

def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
            