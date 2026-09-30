# ============================================
#        PYTHON ARRAY / LIST PROGRAM
# ============================================

numbers = [10, 25, 30, 45, 50, 65, 70, 85, 90, 100]

print("======================================")
print("        PYTHON ARRAY PROGRAM")
print("======================================")

# Display the original array
print("\nOriginal Array:")
print(numbers)

# Display each element
print("\nArray Elements:")
for i in range(len(numbers)):
    print("Index", i, "=", numbers[i])

# Find length
print("\nLength of Array:", len(numbers))

# Access first element
print("First Element:", numbers[0])

# Access last element
print("Last Element:", numbers[-1])

# Add an element
numbers.append(110)
print("\nAfter append:")
print(numbers)

# Insert an element
numbers.insert(2, 999)
print("\nAfter inserting 999 at index 2:")
print(numbers)

# Remove an element
numbers.remove(999)
print("\nAfter removing 999:")
print(numbers)

# Remove last element
removed = numbers.pop()
print("\nRemoved last element:", removed)
print("Array after pop:")
print(numbers)

# Find maximum
print("\nMaximum Element:", max(numbers))

# Find minimum
print("Minimum Element:", min(numbers))

# Find sum
print("Sum of Elements:", sum(numbers))

# Find average
average = sum(numbers) / len(numbers)
print("Average:", average)

# Count elements
print("Number of Elements:", len(numbers))

# Search for an element
search = 50

if search in numbers:
    print("\n", search, "is present in the array.")
else:
    print("\n", search, "is not present in the array.")

# Find index
if search in numbers:
    print("Index of", search, "is:", numbers.index(search))

# Count occurrences
print("Count of 50:", numbers.count(50))

# Sort ascending
numbers.sort()
print("\nArray in Ascending Order:")
print(numbers)

# Sort descending
numbers.sort(reverse=True)
print("\nArray in Descending Order:")
print(numbers)

# Reverse array
numbers.reverse()
print("\nReversed Array:")
print(numbers)

# Slicing
print("\nFirst 5 Elements:")
print(numbers[:5])

print("\nLast 5 Elements:")
print(numbers[-5:])

print("\nElements from index 2 to 6:")
print(numbers[2:7])

# Even numbers
print("\nEven Numbers:")
for number in numbers:
    if number % 2 == 0:
        print(number, end=" ")

# Odd numbers
print("\n\nOdd Numbers:")
for number in numbers:
    if number % 2 != 0:
        print(number, end=" ")

# Square of each number
print("\n\nSquares of Elements:")
for number in numbers:
    print(number, "=", number * number)

# Cube of each number
print("\nCubes of Elements:")
for number in numbers:
    print(number, "=", number * number * number)

# Find largest and smallest using loop
largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print("\nLargest Element:", largest)
print("Smallest Element:", smallest)

# Separate positive and negative numbers
values = [10, -20, 30, -40, 50, -60, 70]

print("\nPositive Numbers:")
for value in values:
    if value > 0:
        print(value, end=" ")

print("\nNegative Numbers:")
for value in values:
    if value < 0:
        print(value, end=" ")

# Copy array
copy_array = numbers.copy()

print("\n\nCopied Array:")
print(copy_array)

# Concatenate arrays
array1 = [1, 2, 3, 4, 5]
array2 = [6, 7, 8, 9, 10]

combined = array1 + array2

print("\nArray 1:")
print(array1)

print("Array 2:")
print(array2)

print("Combined Array:")
print(combined)

# Nested array
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n2D Array:")
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# Matrix elements using indexes
print("\nMatrix Elements:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print("matrix[", i, "][", j, "] =", matrix[i][j])

print("\n======================================")
print("          PROGRAM COMPLETED")
print("======================================")
