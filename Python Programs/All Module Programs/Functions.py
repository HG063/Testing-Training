# Question 1
# Function to find cube of a number

# def cube(num):
#     return num * num * num

# =========================================

# Question 2
# Function to print custamized greeting

# def greet(name):
#     print(f"Hello {name}")

# =========================================

# Question 3
# Function to convert Celsius to Fahrenheit and Fahrenheit to Celsius

# def convert_far_to_cel():
#     print("Enter the temprature in degree Fahrenheit")
#     temp = float(input())
#     inCelsius = (temp - 32) * 5 / 9
#     print(f"{temp} in Celsius is = {round(inCelsius, 2)}")
#
#     print("Enter the temprature in degree Celsius")
#     temp = float(input())
#     inFahrenheit = (temp * 9 / 5) + 32
#     print(f"{temp} in Fahrenheit is = {round(inFahrenheit, 2)}")
# convert_far_to_cel()

# =========================================

# Question 4
# function to check if a string is a palindrome

# def isPalindrome(str):
#     for i in range(0, int(len(str)/2)):
#         if str[i] != str[len(str)-i-1]:
#             return False
#     return True
#
# print(isPalindrome("abcba"))

# =========================================

# Question 5
# function to reverse second half of the string

# def reverse(text):
#     text = list(text)
#     left, right = len(text)//2, len(text)-1
#     while left < right:
#         text[left], text[right] = text[right], text[left]
#         left += 1
#         right -= 1
#     return "".join(text)
#
# print(reverse("abcdef"))

# =========================================
