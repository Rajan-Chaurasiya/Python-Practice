# num = int(input("Enter a number: "))

# rev = 0
# temp = num

# while(num > 0):
#     digit = num % 10;
#     rev = (rev * 10) + digit;
#     num = num // 10;

# if(temp == rev):
#     print("palindrom")
# else:
#     print("not palidrome")

string = input("enter a string :")
if(string == string[::-1]):
    print("The string is palindrome")
else:
    print("The string is not palindrome")



