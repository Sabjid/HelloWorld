# Program 1: Basic arithmetic with integers
a = 5
b = 10
print("Sum:", a + b)

# Program 2: Check if a number is even or odd
number = 7
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# Program 1: Calculate the area of a circle
radius = 3.5
area = 3.14 * radius ** 2
print("Area of circle:", area)

# Program 2: Convert temperature from Celsius to Fahrenheit
celsius = 25.0
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# Program 1: Concatenate two strings
greeting = "Hello"
name = "Alice"
print(greeting + " " + name)

# Program 2: Repeat a string multiple times
word = "Hi"
print(word * 3)

# Program 1: Access elements in a list
fruits = ["apple", "banana", "cherry"]
print("First fruit:", fruits[0])

# Program 2: Add and remove elements from a list
numbers = [1, 2, 3]
numbers.append(4)
numbers.remove(2)
print("Modified list:", numbers)

# Program 1: Create a tuple and access elements
coordinates = (10, 20)
print("X-coordinate:", coordinates[0])

# Program 2: Tuple unpacking
point = (5, 10)
x, y = point
print("x:", x, "y:", y)

# Program 1: Create a dictionary and access elements
person = {"name": "Alice", "age": 25}
print("Name:", person["name"])

# Program 2: Add and update dictionary entries
person["city"] = "New York"
person["age"] = 26
print("Updated person info:", person)


# Program 1: Create a set and add elements
colors = {"red", "green", "blue"}
colors.add("yellow")
print("Colors set:", colors)

# Program 2: Check for element existence
if "green" in colors:
    print("Green is in the set")


# Program 1: Boolean logic with AND and OR
a = True
b = False
print("a AND b:", a and b)
print("a OR b:", a or b)

# Program 2: Check if a number is positive or negative
num = -10
is_positive = num > 0
print("Is number positive?", is_positive)


# Example shapes using strings
print("Square:\n" + "****\n" * 4)
print("Triangle:\n  *  \n *** \n*****")
print("Rectangle:\n" + "*****\n" * 3)
print("Diamond:\n  *  \n *** \n*****\n *** \n  *  ")
print("Arrow:\n  *  \n *** \n*****\n  |  \n  |  ")
print("Heart:\n ** ** \n*******\n ***** \n  ***  \n   *   ")
print("Right-angled triangle:\n*\n**\n***\n****")
print("Cross:\n  *  \n*****\n  *  \n*****\n  *  ")
print("Star:\n  *  \n * * \n*****\n * * \n  *  ")
print("House:\n   *   \n  ***  \n ***** \n*******\n |   |")

