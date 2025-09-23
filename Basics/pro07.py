# Creating a list (array)
numbers = [10, 20, 30, 40, 50]

print(numbers)        # [10, 20, 30, 40, 50]
print(numbers[0])     # Access first element → 10
print(numbers[-1])    # Access last element → 50

# Modifying elements
numbers[2] = 99
print(numbers)        # [10, 20, 99, 40, 50]

# Adding elements
numbers.append(60)    # Add to end
numbers.insert(1, 15) # Add at index 1
print(numbers)

# Removing elements
numbers.remove(99)    # Remove specific value
numbers.pop()         # Remove last element
print(numbers)

# Sort in ascending
numbers.sort()        #sort in ascending order
print(numbers)

# Sort in Reverse
numbers.reverse()     #sort in reverse order
print(numbers)

#length of list
print(len(numbers))

#largest number
print(max(numbers))

#smallest number
print(min(numbers))