class employee:

    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def display(self):
        print(f" the name of employee {self.name} and age is {self.age} and then address is {self.address}")


class developer(employee):
    def __init__(self, name, age, address,salary):
        super().__init__(name,age,address)
        super().display()
        
        self.salary=salary

    def display(self):
         print(f" the name of employee is {self.name} and age is {self.age} and then address is {self.address} and salary is {self.salary}")

d1=developer("anup",25,"putalisadak",25000)
d1.display()       