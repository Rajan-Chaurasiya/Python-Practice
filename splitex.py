filename = input("enter a file name: ")
f_exten = filename.split(".")
print("the extension is: " +repr(f_exten[-1]))