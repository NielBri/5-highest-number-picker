# User input for 5 numbers
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
num3 = float(input("Please enter the third number: "))
num4 = float(input("Please enter the fourth number: "))
num5 = float(input("Please enter the fifth number: "))
# Compare numbers using the if statement and def function
def highest_number(num1, num2, num3, num4, num5):
    # Let us say that num1 is the highest number in order for us to have something to compare
    highest = num1

    # Compare every value to num1 or highest
    if num2 > highest:
        highest = num2

    if num3 > highest:
        highest = num3

    if num4 > highest:
        highest = num4

    if num5 > highest:
        highest = num5

    # We add the return function to let the highest number be replaced to a new one
    return highest

# Add a function that stores the input with the comparison of numbers
# Print out the result
