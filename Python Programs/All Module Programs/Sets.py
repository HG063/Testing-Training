# Question 1
# Remove duplicate values of a list a=[1,2,3,4,1,2,3,10]

# a = [1,2,3,4,1,2,3,10]
# print ("The original list is : " +  str(a))
# res = []
# for i in a:
#     if i not in res:
#         res.append(i)
# print ("The list after removing duplicates : " + str(res))

# =========================================

# Question 2
# What is the output when the following code is run by Python? For sets, do not worry about
# getting the exact order of the output correct.

# s1 = set( [7,9, 12, 7, 9] )
# s2 = set( ['abc', 12, 'b', 'car', 7, 10, 12 ])
# s3 = set( [12, 14, 12, 'ab'] )
# print (s1 & s2)
# print (s1 | s2)
# print ('b' in s2)
# print ('ab' in s2)
# print ('ab' in s3)
# s2.discard(12)
# print ((s1 & s2) ^ s3)

# =========================================

# Question 3
# Given three sets, s1, s2, and s3, write a short segment of Python code to find the values that are
# in exactly one of the three sets. The result should be stored in a set called s. You may NOT use any loops.

# # s1={1,4,5,6,7}
# # s2={2,4,5,6,8}
# # s3={3,4,5,6,7,8}
# s1 = set( [7,9, 12, 7, 9] )
# s2 = set( ['abc', 12, 'b', 'car', 7, 10, 12 ])
# s3 = set( [12, 14, 12, 'ab'] )
# print ((s1 & s2))
# print((s1 & s2) ^ s3)

# =========================================

# Question 4
# Python Program to Count the Number of Vowels Present in a String using Sets

# x=input()
# count=0
# v=("a","e","i","o","u")
# for i in x:
#     if i in v:
#         count=count+1
# print("No of vowers in the string is ", count)

# =========================================

# Question 5
# Take 2 stirngs as input and find out common characters between strings

# x=input('Enter a String ')
# x1 = x.split()
# y=input('Enter another String ')
# y1 = y.split()
# print(set(x)&set(y))

# =========================================

# Question 6
# Take 2 stirngs as input and find out common word between strings

# x=input('Enter a String ')
# x1 = x.split()
# y=input('Enter another String ')
# y1 = y.split()
# print(set(x1)&set(y1))

# =========================================