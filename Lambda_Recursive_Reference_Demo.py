# Example of a lambda function
square = lambda x: x * x
print(square(5))  # Output: 25

# Example of a recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120

# Example of pass by reference
def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]
