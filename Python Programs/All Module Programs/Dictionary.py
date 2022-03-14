# Question 1
# Interchange Key and Value of a dictonary

# heights={'belgian horse': 162,'tiger': 168, 'cat': 58, 'dog': 57, 'cow': 59, 'lion': 109}
# list1=list(heights.keys())
# list2=list(heights.values())
# new_heights=zip(list2,list1)
# print(dict(new_heights))

# =========================================

# Question 2
# Python Program to Concatenate Two Dictionaries Into One

# data1 = {'a':1,'b':2,'c':7,'k':6}
# data2 = {'e':1,'l':2}
# data1.update(data2)
# data1

# =========================================

# Question 3
# Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

# n=int(input("Input a number "))
# sq = dict()
# for x in range(1,n+1):
#     sq[x]=x*x
# print(sq)

# =========================================

# Question 4
# Python Program to Sum All the Items in a Dictionary

# my_dict = {'data1':107,'data2':84,'data3':247}
# print(sum(my_dict.values()))

# =========================================

# Question 5
# Python Program to Multiply All the Items in a Dictionary

# result=1
# for key in my_dict:
#     result=result * my_dict[key]
# print(result)

# =========================================

# Quesiton 6
# Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

# test_string=input("Enter string:")
# l=[]
# l=test_string.split()
# wordfreq=[l.count(p) for p in l]
# print(dict(zip(l,wordfreq)))

# =========================================

# Question 7
# Python Program to Form a Dictionary from an Object of a Class

# class A(object):
#      def __init__(self):
#          self.A=1
#          self.B=2
# obj=A()
# print(obj.__dict__)

# =========================================

# Question 8
# Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character

# test_string=input("Enter string:")
# l=test_string.split()
# d={}
# for word in l:
#     if(word[0] not in d.keys()):
#         d[word[0]]=[]
#         d[word[0]].append(word)
#     else:
#         if(word not in d[word[0]]):
#           d[word[0]].append(word)
# for k,v in d.items():
#         print(k,":",v)

# =========================================