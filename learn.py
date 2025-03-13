# print("hello world")

# import sys # (sys is a built-in module in python)
# print(sys.version)

# if (10 > 4):  # Indentation is important in Python
#     print("10 is greater than 4")

# x = "Hello There" # A variable is created the moment you first assign a value to it.
# y = 10
# print(x,"do you have",y,"apples","?")

# Type casting
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0 
# print(x,y,z)
# print(type(x),type(y),type(z))

# fruit, vegetable, meat = "apple", "carrot", "chicken"
# print(fruit,vegetable,meat)
# x = y = z = "Orange"
# print(x,y,z)

# # collection
# fruits = ["apple", "banana", "cheery"]
# print(fruits)
# x,y,z = fruits
# print(x,y,z)

# # function definition
# first_name = "chinmay"
# last_name = "kubal"

# def print_name():
#     age = 25
#     print("My name is", first_name,last_name,"and " "i am",age,"years old.")

# print_name()

# Learning about python data types :- https://www.w3schools.com/python/python_datatypes.asp (check readme.md)
# Learning about Stings :-  https://www.w3schools.com/python/python_strings.asp (check readme.md)


# # Strings are Arrays
# message = "Hello, World!"
# print(message[7]) # Output: W

# for x in "banana":
#   print(x)


# # Check if a certain phrase or character is present in a string
# text = """Contrary to popular belief, Lorem Ipsum is not simply random text. 
# It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. 
# Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, 
# looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, 
# and going through the cites of the word in classical literature, discovered the undoubtable source.
# Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. 
# This book is a treatise on the theory of ethics, very popular during the Renaissance. 
# The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32."""

# print("Lorem Ipsum" in text) # Output: True


# text = "best things in life are free!"
# if "free" in text:
#     print("Yes, 'free' is present in the text")

# text = "The best things in life are free!"
# if "expensive" not in text:
#   printf("No, 'expensive' is NOT present.")

# # Slicing (https://www.w3schools.com/python/python_strings_slicing.asp)
# slice_me = "Hello, World!"
# print(slice_me[1:6]) # Output: ello,
# print(slice_me[:6]) # Output: Hello,
# print(slice_me[7:]) # Output: World!
# print(slice_me[-6:-1]) # Output: World

# # upper case and lower case, remove whitespace, replace, split
# my_string = " My name is chinmay kubal  "
# print(my_string.upper())
# print(my_string.lower())
# print(my_string.strip()) # The strip() method removes any whitespace from the beginning or the end
# print(my_string.replace("chinmay","charuchandra"))
# print(my_string.split("is")) # The split() method splits the string into substrings if it finds instances of the separator, [' My name ', ' chinmay kubal  ']

# # Format - Strings
# age = 36 # here we dont want to make 36 a string at this place as that will be a permanent change.
# # text1 = "My name is John, I am " + age
# # print(text1) # Output: TypeError: can only concatenate str (not "int") to str
# text2 = f"My name is John, I am {age}"
# text3 = f"myltiply this {2 *5}"
# print(text2) # Output: My name is John, I am 36
# print(text3) # Output: myltiply this 10

# # read the readme.md file for more details on strings