# n = int(input("enter a number :"))

# for i in range(2,n):
#     if (n%i == 0):
#         print("not prime")
#         break
# else:
#     print(" is prime")



# using flag
# num = int(input("Enter a number: "))
# flag = False

# if num > 1:
#     for i in range(2, num):
#         if (num % i == 0):
#             flag = True
#             break

# if flag:
#     print(num, "is not the number prime")
# else:
#     print(num, "is the number prime")

#interval prime
lower = 900
upper = 1000

print("prime number between of", lower, "and", upper, "are: ")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if(num % i == 0):
                break
        else:
            print(num)
