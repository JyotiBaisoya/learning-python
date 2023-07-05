#Write a program to print the following number pattern using a loop.

n = 5  # Define the number of rows

for i in range(1, n + 1):  # Iterate from 1 to n (inclusive)
    for j in range(1, i + 1):  # Iterate from 1 to i (inclusive) for each row
        print(j, end=" ")
    print()  # Move to the next line after printing each row


# Display numbers from a list using loop
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break  # Stop the loop if the number is greater than 500
    if num > 150:
        continue  # Skip the number if it is greater than 150 and move to the next iteration
    if num % 5 == 0:
        print(num)


# Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"

mid_index = len(s1) // 2
s3 = s1[:mid_index] + s2 + s1[mid_index:]

print(s3)


#Arrange string characters such that lowercase letters should come first

str1 = "PyNaTive"

lowercase = sorted([char for char in str1 if char.islower()])
uppercase = sorted([char for char in str1 if char.isupper()])

sorted_str = "".join(lowercase + uppercase)
print(sorted_str)


#: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

new_list = []
min_len = min(len(list1), len(list2))

for i in range(min_len):
    new_list.append(list1[i] + list2[i])

if len(list1) > len(list2):
    new_list += list1[min_len:]
else:
    new_list += list2[min_len:]

print(new_list)


#Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = []

for item1 in list1:
    for item2 in list2:
        result.append(item1 + item2)

print(result)


#: Iterate both lists simultaneously

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

list2_reverse = list2[::-1]  # Reverse the order of list2

for item1, item2 in zip(list1, list2_reverse):
    print(item1, item2)


# Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

result = {employee: defaults for employee in employees}

print(result)


#Modify the tuple

tuple1 = (11, [22, 33], 44, 55)

list1 = list(tuple1)  # Convert the tuple to a list
list1[1][0] = 222  # Modify the first item of the nested list
tuple1 = tuple(list1)  # Convert the list back to a tuple

print("tuple1:", tuple1)


