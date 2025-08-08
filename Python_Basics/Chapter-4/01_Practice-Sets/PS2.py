# Write a program to accept marks of 6 students and display them in a sorted manner.

m1 = int(input("Enter Your Marks : "))
m2 = int(input("Enter Your Marks : "))
m3 = int(input("Enter Your Marks : "))
m4 = int(input("Enter Your Marks : "))
m5 = int(input("Enter Your Marks : "))
m6 = int(input("Enter Your Marks : "))

list = [m1, m2, m3, m4, m5, m6]
list.sort()
print(list)