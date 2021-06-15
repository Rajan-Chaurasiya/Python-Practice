#using temp variable 

#num1 = input("enter a first number:")
#num2 = input("enter a second number:")

#print("value of num1 before swap:", num1)
#print("value of num2 before swap:", num2)

#temp = num1
#num1 = num2
#num2 = temp

#print("value of num1 after swap:",num1)
#print("value of num2 after swap:",num2)

#without using temp variable

num1 = input("enter a first number:")
num2 = input("enter a second number:")

print("value of num1 before swap:", num1)
print("value of num2 before swap:", num2)

num1, num2 = num2, num1

print("value of num1 after swap:",num1)
print("value of num2 after swap:",num2)