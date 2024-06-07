from typing import List
import csv

#define classes

class Vehicle:
    def __init__(self, brand, model, year, color, price):
        self.model = model
        self.brand = brand
        self.year = year
        self.color = color
        self.price = price

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, color, price):
        super().__init__(brand, model, year, color, price)
    def __repr__(self):
        return f"Motorcycle\t{self.brand}\t{self.model}\t{self.year}\t{self.color}\t{self.price}\tn/a"
        
class Car(Vehicle):
    def __init__(self, brand, model, year, color, price, doors):
        super().__init__(brand, model, year, color, price)
        self.doors = doors
    def foo(self):
        print(f"foo: {self.model}")
    def __repr__(self):
        return f"Car\t{self.brand}\t{self.model}\t{self.year}\t{self.color}\t{self.price}\t{self.doors}"
        

            


class Inventory:
    data: List[Vehicle] = []
    
    def __init__(self, file):
        self.file = file
        self.__load(self.file)

    def __load(self, file):
        with open(file, "r") as inventory_file:
            rd = csv.DictReader(inventory_file, delimiter="\t")
            for row in rd:
                if row['type'] == "Car":
                    self.data.append(Car(row['brand'], row['model'], row['year'], row['color'], row['price'], row['doors']))
                elif row['type'] == "Motorcycle":
                    self.data.append(Motorcycle(row['brand'], row['model'], row['year'], row['color'], row['price']))
    
    def add(self, vehicle):
        with open(self.file, 'a') as inventory_file:
            inventory_file.write('\n'+str(vehicle))
        self.data.append(vehicle)
                
    def __repr__(self):
        output = ''
        output += 'type\tbrand\tmodel\tyear\tcolor\tprice\tdoors'
        for row in self.data:
            output += '\n' + str(row)
        return output
            
inventory = Inventory('inventory.tsv')
inventory.add(Car('Aoodi', 'A1', '1900', 'Gray', '20000', '4'))
print(inventory)
