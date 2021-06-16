class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name;
        self.product = product;

    def getInfo(self):
        print(f"the name of {self.company} programmer is {self.name} and the product is {self.product}")

Rajan = Programmer("Rajan","Skype")
Rajan.getInfo()


        