#  1. Equality vs Identity
# Both operators look similar in purpose, but they answer two different questions.
# - == checks whether two objects have equal values.
# - is checks whether two variables refer to the exact same object.
# A. Equality operator (==)
# Suppose we create two lists:
# a = [10, 20, 30]b = [10, 20, 30]print(a == b)
#
#
#
# Output:
# True
#
#
# Why?
#
# Because both lists contain the same values in the same order.
#
# Python compares their contents, not whether they are the same object.
# B. Identity operator (is)
# Now consider:
# a = [10, 20, 30]b = [10, 20, 30]print(a is b)
#
#
#
# Output:
# False
#
#
# Why?
#
# Although both lists contain identical values, Python created two separate list objects.
# Visualise the difference
# OBJECT 1
# a → [10, 20, 30]
#
#
# OBJECT 2
# b → [10, 20, 30]
#
#
# a == b
# True
#
# a is b
# False
#
# Same contents, different objects.
# C. When will both return True?
# a = [10, 20, 30]b = aprint(a == b)print(a is b)
#
#
#
# Output:
# True
# True
#
#
# Because b = a does not create another list. Both variables refer to the same object.
# 2. Real-world application
# Imagine you are developing an employee management system using Django.
#
# You retrieve an employee's department:
# department = None
#
#
#
# You want to check whether the department is missing.
# if department is None:    print("Department not assigned")
#
#
#
# Why use is None?
#
# Because None is a special singleton object in Python. The recommended way to check whether a value is None is using is None, not == None.
#
# This is a convention you will frequently encounter in professional Python code.
# 3. Important comparison
# Operator	Purpose
# ==	Compares values
# is	Compares object identity
# !=	Checks whether values differ
# is not	Checks whether objects are different
#
# Remember: Never use is to compare ordinary strings, numbers or list contents. Use == for value comparisons.