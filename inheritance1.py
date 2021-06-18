# class employee:
#     company = "Google"

#     def showDetails(self):
#         print("This is an employee")

# class programmer(employee):
#     language = "python"

#     def getLanguage(self):
#         print(f"the language is {self.language}")

#     def showDetails(self):
#         print("this is a progammer")

# e = employee()
# e.showDetails()
# print(e.company)
# p = programmer()
# p.getLanguage()
# p.showDetails()


# Single level inheritance

# class animal():
#     def speak(self):
#         print("Animal speaking")
    
# class dog(animal):
#     def bark(self):
#         print("dog barking")

# d = dog()
# d.speak()
# d.bark()

#Multiple inheritance

class calculation1:
    def submmation(self, a, b):
        return a+b;
    
class calculation2:
    def multiplication(self, a, b):
        return a*b; 

class derived(calculation1, calculation2):
    def devide(self, a, b):
        return a/b;

d = derived()
print(d.submmation(10, 20))
print(d.multiplication(10, 20))
print(d.devide(10, 20))
