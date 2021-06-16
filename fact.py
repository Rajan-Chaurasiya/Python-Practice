def fact(x):
    f = 1
    for i in range(1,x+1):
        f = f*i
    return f

n = int(input("enter a number: "))
result = fact(n)
print(result)

# n = 6
# for i in range(n):
#     print("*" * (n-i))



