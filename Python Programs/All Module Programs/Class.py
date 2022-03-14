# Question 1
# Python Program to Find the Area of a Rectangle Using Classes

# class Rectangle:
#     def __init__(self, length, bredth):
#         self.l = length
#         self.b = bredth
#
#     def calculateArea(self):
#         return self.l * self.b
# r1 = Rectangle(10, 40)
# print(r1.calculateArea())

# =========================================

# Question 2
# Python Program to Append, Delete and Display Elements of a List Using Classes

# class ListClass:
#     def __init__(self, *listElements):
#         self.list = [ele for ele in listElements]
#
#     def append(self, element):
#         self.list.append(element)
#
#     def delete(self, index=None):
#         if index:
#             return self.list.pop(index)
#         return self.list.pop()
#
#     def display(self):
#         for ele in self.list:
#             print(ele, end=", ")
#         print()
# l1 = ListClass(1,2,3,4)
# l1.display()
# l1.append(5)
# l1.display()
# print(l1.delete())
# l1.display()

# =========================================

# Question 3
# Python Program to Create a Class and Compute the Area and the Perimeter of the Circle

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def getArea(self):
#         return round(3.14 * (self.radius * self.radius), 2)
#
#     def getParameter(self):
#         return round(2 * 3.14 * self.radius, 2)
#
# c1 = Circle(5)
# print(c1.getArea())
# print(c1.getParameter())

# =========================================

# Question 4
# Python Program to compare 2 objects

# class Compare:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def areEqualValue(self):
#         return self.a == self.b
#
#     def areSameObject(self):
#         return self.a is self.b
# a = [1,2,3]
# b = [1,2,3]
# c1 = Compare(a,b)
# print(c1.areEqualValue())
# print(c1.areSameObject())

# =========================================