# Question 1
# Reverse the tuple

# tuple1 = (10, 20, 30, 40, 50)
# tuple1 = tuple1[::-1]
# print(tuple1)

# =========================================

# Question 2
# Swap two tuples in Python

# tuple1 = (11, 22)
# tuple2 = (99, 88)
# tuple1, tuple2 = tuple2, tuple1
# print(tuple2)
# print(tuple1)

# =========================================

# Question 3
# Sort a tuple of tuples by 2nd item

# tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
# print(tuple1)

# =========================================

# Question 4
# Elements frequency in Tuple

# from collections import Counter
# test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)
# print("The original tuple is : " + str(test_tup))
# res = dict(Counter(test_tup))
# print("Tuple elements frequency is : " + str(res))

# =========================================

# Question 5
# Sum of tuple elements

# test_tup = (7, 8, 9, 1, 10, 7)
# print("The original tuple is : " + str(test_tup))
# res = sum(list(test_tup))
# print("The summation of tuple elements are : " + str(res))

# =========================================

# Question 6
# Converting List to tuple and print it's type

# list1=['a',1,100,233]
# t=tuple(list1)
# print (t)
# print(type(t))

# =========================================

# Question 7
# Concat two tuples

# tuple1=(1,3,444,55)
# tuple3=tuple1 + (2,777,"string")
# print(tuple3)

# =========================================