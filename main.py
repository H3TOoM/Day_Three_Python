## Indexing Strings in Python [Start : End : Steps]

# credit_number = "1234-5678-9012-3456"
# print(f"First digit: {credit_number[0]}") # Accessing the first character
# print(f"Last digit: {credit_number[-1]}") # Accessing the last character

# print(f"First four digits: {credit_number[0:4]}") # Slicing the first four characters
# print(f"Last four digits: {credit_number[-4:]}") # Slicing the last four characters

# print(f"Every second digit: {credit_number[::2]}") # Slicing with a step of 2

## Exercise: Print the last four digits of a credit card number
# last_four_digits = credit_number[-4:]
# print(f"Last four digits of the credit card: {last_four_digits}") # Output: 3456

## Exercise: Reverse a string
# credit_number_reversed = credit_number[::-1]
# print(f"Reversed credit card number: {credit_number_reversed}") # Output: 6543-2109-8765-4321

## Format Specifiers in Python = {value:flags} format a value based on what flag are intersted
# .(number)f = formats a float to a fixed number of decimal places
# :(number) = allocate that many spaces
# :03 = alocate and zero pad that many spaces
# :< = left align
# :> = right align
# :^ = center align
# :+ = use a plus sign for positive numbers
# := = place the sign to the leftmost position
# :  = insert a space before positive numbers
# :, = use a comma as a thousands separator

# price_one = 49.99
# price_two = 9.99
# price_three = 999.99

# print(f"Price One: {price_one:.2f}") # Output: Price One: 49.99
# print(f"Price Two: {price_two:06.2f}") # Output: Price Two: 009.99
# print(f"Price Three: {price_three:>10.2f}") # Output: Price Three:     999.99
# print(f"Price One Centered: {price_one:^10.2f}") # Output: Price One Centered:   49.99
# print(f"Price One with Sign: {price_one:+.2f}") # Output: Price One with Sign: +49.99
# print(f"Price Two with Sign: {price_two:+.2f}") # Output: Price Two with Sign: +9.99
# print(f"Price Three with Sign: {price_three:+.2f}") # Output: Price Three with Sign: +999.99
# print(f"Price One with Space: {price_one: .2f}") # Output: Price One with Space:  49.99
# print(f"Price Two with Space: {price_two: .2f}") # Output: Price Two with Space:  9.99
# print(f"Price Three with Space: {price_three: .2f}") # Output: Price Three with Space:  999.99
# print(f"Price Three with Comma: {price_three:,.2f}") # Output: Price Three with Comma: 999.99
# print(f"Large Number with Comma: {1234567890:,}") # Output: Large Number with Comma: 1,234,567,890


## While Loops in Python
# name = input("Enter your name: ")
# while name.strip() == "": # Strip to remove any leading/trailing whitespace
#     print("You didn't enter a name. Please try again.")
#     name = input("Enter your name: ")
# print(f"Hello, {name}!")

# age = int(input("Enter your age Bro: "))
# while age < 0 and age == 0 and age > 120:
#     print("Please enter a valid age Bro.")
#     age = int(input("Enter your age Bro: "))

# print(f"You are {age} years old Bro :).")

# food = input("Enter your favorite food (q to quit): ")
# while not food == "q":
#     print(f"{food} is a great choice!")
#     food = input("Enter your favorite food (q to quit): ")
# print("Goodbye! Enjoy your meal!")

# num = int(input("Enter a number between 1 and 10: "))
# while num < 1 or num > 10:
#     print("Invalid number. Please try again.")
#     num = int(input("Enter a number between 1 and 10: "))
# print(f"Thank you! You entered {num}.")


## Exercise: Python Compound Interest Calculator => A = P (1 + r/n)^(nt)
## Without While Loop
# principal = float(input("Enter the principal amount (P): "))
# rate = float(input("Enter the annual interest rate (r) in percentage: ")) / 100
# times_compounded = int(input("Enter the number of times interest is compounded per year (n): "))
# years = int(input("Enter the number of years the money is invested (t): "))
# amount = principal * (1 + rate / times_compounded) ** (times_compounded * years)
# print(f"The amount after {years} years is: ${amount:.2f}")

## With While Loop
# principal = 0
# rate = 0
# time = 0

# while principal <= 0:
#     principal = float(input("Enter the principal amount (P): "))
#     if principal <= 0:
#         print("Principal amount must be greater than 0. Please try again.")

# while rate <= 0:
#     rate = float(input("Enter the annual interest rate (r) in percentage: ")) / 100
#     if rate <= 0:
#         print("Interest rate must be greater than 0. Please try again.")

# while time <= 0:
#     time = int(input("Enter the number of years the money is invested (t): "))
#     if time <= 0:
#         print("Number of years must be greater than 0. Please try again.")

# total_amount = principal * pow((1 + rate), time)
# print(f"The amount after {time} years is: ${total_amount:.2f}")


## Today I Learned:
# - How to index and slice strings in Python using [start:end:step] notation.
# - Various format specifiers in Python for formatting numbers and strings.
# - How to use while loops in Python to repeatedly execute a block of code until a condition
#   is met.
# - Implemented a compound interest calculator with input validation using while loops.

## Happy Coding :)
## This is the end of main.py
## Alaways remember: "Code is like humor. When you have to explain it, it’s bad." – Cory House
## Allhu Akbar :) 
## See you in the next lesson :)
## Goodbye!