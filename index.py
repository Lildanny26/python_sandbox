# Activity 1

# Section 1 
# Question 1 Create two variables. One should be a string data type, and the other should be of type int. Use a single print statement to print both variables.

# cool_string = 'Hello World'
# print(cool_string)

# Question 2 Create a Python function that prints a greeting with a name as the parameter. Invoke the function with a name argument of your choosing.

# def greet(name):
    # print(f'Hello, {name}! Welcome Bitch!')

# greet('Daddy')

# Section 2 
# Question 3 Create a list of your favorite movies with at least 4 elements.

# marvel_superhero = ['SpiderMan', 'Thor', 'IronMan', 'DoctorStrange']

# Question 4 Use a print statement to print the list item at the index of 1.

# marvel_superhero = ['SpiderMan', 'Thor', 'IronMan', 'DoctorStrange']
# print(marvel_superhero[0])

# Question 5: Append a movie to the end of your list. Use a print statement to print this ammended list.

# marvel_superhero = ['SpiderMan', 'Thor', 'IronMan', 'DoctorStrange']

# marvel_superhero.append('DeadPool')

# print(marvel_superhero)

# Section 3
# Question 6: Create a dictionary named 'cellphone' with 2 key:value pairs that are the properties of your cellphone.
# The keys should be: "color" and "number".
# Fill out the values on your own:

# cellphone = {
    # "color": 'Blue',
    # "number": "123-456-7890"
# }

# Question 7 Access a value from inside the dictionary (Try to print the value of the 'color' property).

# cellphone = {
    # "color": 'Blue',
    # "number": "123-456-7890"
# }

# print(cellphone['number'])

# Section 4
# Question 8: Create a variable and store a string with multiple words in it.

# my_string = 'hello i am cool'

# Question 9: Utilize the method that capitalizes the first letter of each word in your string - store this new string in a new variable. Use a print statement to print the new string.

# my_string = 'hello i am cool'
# capitalized_string = my_string.title()

# print(capitalized_string)

#Bonus
# students_in_order = {
  # 1: {'name': 'Esteban', 'age': '27', 'eye color': 'blue'},
  # 2: {'name': 'Jackson', 'age': '22', 'eye color': 'brown'},
  # 3: {'name': 'Zayn', 'age': '26', 'eye color': 'green'}
# }

# Question 10 A: Write a print function that outputs the second student in the dictionary.

# print(students_in_order[2])

# Question 10 B: Write a print statement that outputs the name "Zayn" using the dictionary.

# print(students_in_order[3]['name'])

# Question 10 C: Write a print statment that outputs the age of Esteban from the dictionary.

# print(students_in_order[1]['age'])





# Activity 2

#Section 1 - sets and tuples:
#Pre-Question: Take a look at this JavaScript Array:
# let javaScriptArray = [12, 55, 33, 40, 55, 33, 20, 12]

# How would you remove duplicates from this JavaScript Array? Take a few minutes to consider what steps are necessary to iterate through this array in JavaScript and remove the duplicates values.

java_script_array = [12, 55, 33, 40, 55, 33, 20, 12]
unique_list = list(set(java_script_array))

print(unique_list)

# What advantages are available when we're working with Python? If this Array was instead a set, we wouldn't be able to store multiple values in it. Uncomment the identical set below and run the print statement. What did you notice in the console return?

my_set = {12, 55, 33, 40, 55, 33, 20, 12}

print(my_set)

#Question 1a: Create a set of your own with at least 3 different elements.

my_numbers = {1, 2, 3, 4, 5}

#Question 1b: Add an item to the set that you just created.

my_numbers = {1, 2, 3, 4, 5}

my_numbers.add(6)


#Question 1c: Print the set with the new data that you added to it:

my_numbers = {1, 2, 3, 4, 5}

my_numbers.add(6)

print(my_numbers)


#Question 2a: Create a tuple with at least 3 elements inside of it.

my_tuple = (10, "hello", 3.14)

#Question 2b: Print the tuple you just created.

my_tuple = (10, "hello", 3.14)

print(my_tuple)


#Section 2 - loops:

# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# Question 3: Use a for loop to iterate through the 'days' list above and print the days of the week:

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in days:
    print(day)

x = 10
add_list = [10, 6, 12, 4, 5]

# Question 4: Uncomment the list and variable x above.  Loop through add_list and add each value to x. Print the value of x at each increment:

for value in add_list:
    x += value
print(x)


# Question 5: While Loops 

#Declare an iterator variable (set to the number 1) and write a While loop that adds 5 to the value of the variable starting_value as long as the iterator is under 10:

starting_value = 5
iterator = 1 

while iterator < 10:
    starting_value += 5
    iterator += 1
    print(starting_value)




#Section 3 - conditionals: if, elif, else statements

favorite_movie = "SpiderMan"    
#Question 6a: Uncomment the favorite_movie variable above and change the value to the title of your favorite movie
#Below, write a conditional statement that prints the string "that's a great movie" if the favorite_movie variable equals your favorite movie.
#Otherwise (else), print the string "that's not my favorite movie".  
#Mess around with the value of the favorite_movie variable and trigger both conditional responses:

if favorite_movie == "SpiderMan":
    print("That's a great movie")
else:
    print("That's not my favorite movie")


#Question 6b: Uncomment the movie_list variable below and implement a for loop that iterates through each item in the list. 
#If the item is a blueberry (or another fruit), print "item is a fruit and not movie"; 
#if the item is a car manufacturing company like Toyota, print "item is a car and not a movie"; 
#otherwise, just print the movie in the list:

movie_list = ["Inception", "blueberries", "Toyota", "Good Will Hunting"]

fruits = ["blueberries", "apple", "banana", "orange"]
car_manufacturers = ["Toyota", "Ford", "BMW", "Honda"]

for item in movie_list:
    if item in fruits:
        print(f"{item} is a fruit and not a movie")
    elif item in car_manufacturers:
        print(f"{item} is a car and not a movie")
    else:
        print(item)



#BONUS - conditional and operators practice:
# a = 5
# b = 5
# c = 12
#Question 7a: Use the correct operator to add variables a & c:

a = 5
c = 12 

sum_results = a + c
print(sum_results)

#Question 7b: Use the correct operator to subtract variables b & c:

b = 5
c = 12

difference_results = b - c
print(difference_results)

#Question 7c: Use the correct comparison operator that shows if variables a & b equal each other:

a = 5
b = 5

are_equal = a == b 
print(are_equal)

#Question 7d: Use the correct operator to find the quotient of variables c & a

c = 12
a = 5

quotient = c / a 
print(quotient)

#Question 7e: Use the correct operator to find if variables c & b are not equal to each other:

c = 12
b = 5

are_not_equal = c != b
print(are_not_equal)





#Activity 3 
# Function Definition Practice:
# Define functions according to the following prompts.


# 1. Function that accepts no arguments. It's called say_hello and returns nothing, just prints 'hello'.

def say_hello(): 
    print('hello')

# 2. a 'sum' function that accepts two integers and returns the sum.

def add(a, b):
    return(5 + 5)

# 3. an 'average' function that accepts two numbers and returns the average.

def average(num1, num2):
    return(num1 + num2) / 2

# 4. A function that accepts a first name and a last name and formats it to "{last_name}, {first_name}" (returns a string).

def format_name(first_name, last_name):
    return f"(last_name), (first_name)"

# 5. A function that accepts a first name, last name, graduation year, and student number and returns those four items together in a list.

def student_info(first_name, last_name, graduation_year, student_number):
    return [first_name, last_name, graduation_year, student_number]

# 6. A function that accepts an integer and returns whether it is above 18 or not (Boolean).

def is_above_18(age):
    return age > 18

#7. A function that accepts a string and prints the string in reverse (no return value).

def print_reverse(s):
    print(s[::-1])