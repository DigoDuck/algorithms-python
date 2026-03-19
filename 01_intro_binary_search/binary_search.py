
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high: # While the search is not limited to just one element
        middle = (low + high) // 2
        guess = list[middle]
        if guess == item: # If the item is found, it returns its position.
            return middle
        if guess > item: # If the number is less than half, ignore the right half.
            high = middle -1
        else:   # If the number is greater than half, ignore the left half.
            low = middle + 1
    return None # Returns None if the item is not found.

my_list = [1,3,5,7,9]

print(binary_search(my_list, 3)) #1
print(binary_search(my_list, -1)) #None