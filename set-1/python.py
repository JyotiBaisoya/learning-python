# Hello, World!: Write a Python program that prints "Hello, World!" to the console.

print("Hello World")

#Data Type Play: Create variables of each data type 
#(integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.

# Integer
my_integer = 10

# Float
my_float = 3.14

# String
my_string = "Hello, World!"

# Boolean
my_boolean = True

# List
my_list = [1, 2, 3, 4, 5]

# Tuple
my_tuple = (6, 7, 8, 9, 10)

# Dictionary
my_dictionary = {"name": "John", "age": 25, "city": "New York"}

# Set
my_set = {1, 2, 3, 4, 5}

# Print types and values
print("Type of my_integer:", type(my_integer), ", value:", my_integer)
print("Type of my_float:", type(my_float), ", value:", my_float)
print("Type of my_string:", type(my_string), ", value:", my_string)
print("Type of my_boolean:", type(my_boolean), ", value:", my_boolean)
print("Type of my_list:", type(my_list), ", value:", my_list)
print("Type of my_tuple:", type(my_tuple), ", value:", my_tuple)
print("Type of my_dictionary:", type(my_dictionary), ", value:", my_dictionary)
print("Type of my_set:", type(my_set), ", value:", my_set)


# Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.

#to create a list
numbers = [x for x in range(1, 11)]

#to add into list
numbers.append(0)

#to remove from list
numbers.remove(2)

#to sort the list
numbers.sort()

# print(numbers)--->you can check the list using this


#Write a Python program that calculates and prints the sum and average of a list of numbers.

#to sum the numbers of a list

sum_of_numbers = sum(numbers)

avg_of_numbers = sum_of_numbers/len(numbers)

#print(sum_of_numbers,avg_of_numbers)-----> by using this i can see the output in console of both sum and average

##Write a Python function that takes a string and returns the string in reverse order.

# to reverse the string we have three different ways :

#1.
original_string = "Hello, Jyoti!"
reversed_string = original_string[::-1]
print(reversed_string)

#2.
original_string2 = "Hello, Himanshu!"
reversed_string2 = original_string2[::-1]
print(reversed_string2)

#3
original_string3 = "Hello, Vipin!"
reversed_string3 = ''
for char in original_string3:
    reversed_string3 = char + reversed_string
print(reversed_string3)

#Write a Python program that counts the number of vowels in a given string.


def count_vowels(string):
    vowel_count = 0
    vowels = "aeiouAEIOU"  

    for char in string:
        if char in vowels:
            vowel_count += 1

    return vowel_count



input_string = "Hello"
result = count_vowels(input_string)
print("Number of vowels:", result)


#Write a Python function that checks whether a given number is a prime number.

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True



input_number = 13
if is_prime(input_number):
    print(input_number, "is a prime number")
else:
    print(input_number, "is not a prime number")


#Write a Python function that calculates the factorial of a number.

def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result


input_number = 5
result = factorial(input_number)
print("Factorial of", input_number, "is", result)


#Write a Python function that generates the first n numbers in the Fibonacci sequence.

def generate_fibonacci(n):
    fibonacci_sequence = []

    if n >= 1:
        fibonacci_sequence.append(0)

    if n >= 2:
        fibonacci_sequence.append(1)

    for i in range(2, n):
        next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence


# Test the function
input_n = 5
fibonacci_numbers = generate_fibonacci(input_n)
print(fibonacci_numbers)


#Use list comprehension to create a list of the squares of the numbers from 1 to 10.

my_list = [1, 2, 3, 4, 5,6,7,8,9,10]
squared_list = [x**2 for x in my_list]
print(squared_list)


