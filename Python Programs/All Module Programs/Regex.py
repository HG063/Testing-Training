import re
# Question 1
# Write a Python program to check that a string contains only a certain set of characters
# (in this case a-z, A-Z and 0-9).

# def is_allowed_specific_char(string):
#     charRe = re.compile(r'[^a-zA-Z0-9]')
#     string = charRe.search(string)
#     return not bool(string)
# print(is_allowed_specific_char("ABCDEFabcdef123450"))
# print(is_allowed_specific_char("*&%@#!}{"))

# =========================================

# Question 2
# Write a Python program that matches a string that has an a followed by zero or more b's

# match = re.search(r'\wb*', 'pppppbbbbbbg')
# match.group()

# =========================================

# Question 3
# Write a Python program that matches a string that has an a followed by one or more b's.

# match = re.search(r'\wb+', 'pppppbbbbbbg')
# match.group()

# =========================================

# Question 4
# Write a Python program that matches a string that has an a followed by zero or one 'b'.

# match = re.search(r'\w+b?', 'pppppbg')
# match.group()

# =========================================

# Question 5
# Write a Python program that matches a string that has an a followed by three 'b

# match = re.search(r'\wb{3}', 'ppppbbbg')
# match.group()

# =========================================

# Question 6
# Write a Python program that matches a word containing 'z'.

# if re.search(r'\w*z.\w*', 'The quick brown fox jumps over the lazy dog'):
#     print('True')
# else:
#     print('False')

# =========================================

# Question 7
# Write a Python program that matches a word containing 'z', not start or end of the word.

# if re.search(r'\Bz\B', 'The quick brown fox jumps over the lazy dog'):
#     print('True')
# else:
#     print('False')

# =========================================

# Question 8
# Write a Python program to remove leading zeros from an IP address.

# ip = "216.08.094.196"
# string = re.sub('\.[0]*', '.', ip)
# print(string)

# =========================================

# Question 9
# Write a Python program to check for a number at the end of a string.

# if re.search(r".*[0-9]$",'abcdef6'):
#     print('True')
# else:
#     print('False')

# =========================================

# Question 10
# Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string. "Exercises number 1, 12, 13, and 345 are important"

# results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
# print("Number of length 1 to 3")
# for n in results:
#      print(n.group(0))

# =========================================

# Question 11
# Write a Python program to find the occurrence and position of the substrings within a string.

# text = 'Python exercises, PHP exercises, C# exercises'
# pattern = 'exercises'
# for match in re.finditer(pattern, text):
#     s = match.start()
#     e = match.end()
#     print('Found "%s" at %d:%d' % (text[s:e], s, e))

# =========================================

# Question 12
# Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# print(re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1','2020-02-02'))

# =========================================

# Question 13
# Write a Python program to separate and print the numbers of a given string.

# result="The god of the world's leading religion. The chief temple is in the holy"
# result.split(" ",5)

# =========================================

