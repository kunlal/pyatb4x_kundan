

# ### Task #8
#
# ✅ Triangle Classifier:
#
# Write a program that classifies a triangle based on its side lengths.
#
# Given three input values representing the lengths of the sides,
#
# determine if the triangle is equilateral (all sides are equal),
#
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
#
# Use an if-else statement to classify the triangle.

s1 = int(input("Provide side 1 of the triangle"))
s2 = int(input("Provide side 2 of the triangle"))
s3 = int(input("Provide side 3 of the triangle"))

if s1 == s2 == s3:
    print("Equilateral")
elif s1 == s2 or s1 == s3 or s2==s3:
    print("isosceles")
else:
    print("scalene")

