n = int(input("enter a number:"))
sum = 0
order = len(str(n))
temp = n
while(n>0):
    digit = n % 10
    sum += digit**order
    n = n//10

if(temp == sum):
    
    print("This number is armstrong")
else:
    print("This number is not armstrong")

