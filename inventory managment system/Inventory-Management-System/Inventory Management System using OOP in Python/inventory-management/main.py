from abc import ABC, abstractmethod
import json
from datetime import datetime

# Custom error when stock is not enough
class OutOfStockError(Exception):
    pass

# Custom error when product ID already exists
class DuplicateProductError(Exception):
    pass

# Base class for all products
class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    # Add stock
    def restock(self, amount):
        self.stock += amount

    # Sell stock
    def sell(self, quantity):
        if quantity > self.stock:
            raise OutOfStockError("Not enough stock!")
        self.stock -= quantity

    # Total value of stock
    def get_total_value(self):
        return self.price * self.stock

    # Force child classes to print info
    @abstractmethod
    def __str__(self):
        pass

# Electronics product
class Electronics(Product):
    def __init__(self, product_id, name, price, stock, warranty, brand):
        super().__init__(product_id, name, price, stock)
        self.warranty = warranty
        self.brand = brand

    def __str__(self):
        return f"[Electronics] {self.name} (Brand: {self.brand}, Warranty: {self.warranty} years, Price: ${self.price}, Stock: {self.stock})"

# Grocery product
class Grocery(Product):
    def __init__(self, product_id, name, price, stock, expiry_date):
        super().__init__(product_id, name, price, stock)
        self.expiry_date = expiry_date

    def is_expired(self):
        return datetime.strptime(self.expiry_date, '%Y-%m-%d') < datetime.now()

    def __str__(self):
        status = "Expired" if self.is_expired() else "Fresh"
        return f"[Grocery] {self.name} (Expiry: {self.expiry_date}, {status}, Price: ${self.price}, Stock: {self.stock})"

# Clothing product
class Clothing(Product):
    def __init__(self, product_id, name, price, stock, size, material):
        super().__init__(product_id, name, price, stock)
        self.size = size
        self.material = material

    def __str__(self):
        return f"[Clothing] {self.name} (Size: {self.size}, Material: {self.material}, Price: ${self.price}, Stock: {self.stock})"

# Inventory to manage products
class Inventory:
    def __init__(self):
        self.products = {}  # Dictionary to store products

    # Add product
    def add_product(self, product):
        if product.product_id in self.products:
            raise DuplicateProductError("Product ID already exists!")
        self.products[product.product_id] = product

    # Sell product
    def sell_product(self, product_id, quantity):
        product = self.products.get(product_id)
        if product:
            product.sell(quantity)

    # List all products
    def list_all_products(self):
        return list(self.products.values())

    # Search by name
    def search_by_name(self, name):
        return [p for p in self.products.values() if name.lower() in p.name.lower()]

    # Save inventory to file
    def save_to_file(self, filename):
        data = []
        for p in self.products.values():
            if isinstance(p, Electronics):
                data.append({"type": "Electronics", **p.__dict__})
            elif isinstance(p, Grocery):
                data.append({"type": "Grocery", **p.__dict__})
            elif isinstance(p, Clothing):
                data.append({"type": "Clothing", **p.__dict__})
        with open(filename, 'w') as f:
            json.dump(data, f)

    # Load inventory from file
    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            for item in data:
                type_ = item.pop("type")
                if type_ == "Electronics":
                    p = Electronics(**item)
                elif type_ == "Grocery":
                    p = Grocery(**item)
                elif type_ == "Clothing":
                    p = Clothing(**item)
                self.products[p.product_id] = p

# Start menu
if __name__ == "__main__":
    inventory = Inventory()

    while True:
        print("\n===== Inventory Menu =====")
        print("1. Add Product")
        print("2. Sell Product")
        print("3. List Products")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Load Inventory")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':  # Add product
            print("Type: 1. Electronics 2. Grocery 3. Clothing")
            t = input("Type: ")
            pid = int(input("ID: "))
            name = input("Name: ")
            price = float(input("Price: "))
            qty = int(input("Stock: "))

            try:
                if t == '1':
                    brand = input("Brand: ")
                    warranty = int(input("Warranty (years): "))
                    p = Electronics(pid, name, price, qty, warranty, brand)
                elif t == '2':
                    expiry = input("Expiry Date (YYYY-MM-DD): ")
                    p = Grocery(pid, name, price, qty, expiry)
                elif t == '3':
                    size = input("Size: ")
                    material = input("Material: ")
                    p = Clothing(pid, name, price, qty, size, material)
                else:
                    print("Invalid Type!")
                    continue

                inventory.add_product(p)
                print("Product Added!")
            except DuplicateProductError as e:
                print(e)

        elif choice == '2':  # Sell product
            pid = int(input("Enter Product ID: "))
            qty = int(input("Enter quantity: "))
            try:
                inventory.sell_product(pid, qty)
                print("Sold!")
            except OutOfStockError as e:
                print(e)

        elif choice == '3':  # List all products
            for p in inventory.list_all_products():
                print(p)

        elif choice == '4':  # Search product
            name = input("Enter name to search: ")
            results = inventory.search_by_name(name)
            for p in results:
                print(p)

        elif choice == '5':  # Save to file
            inventory.save_to_file("inventory.json")
            print("Saved!")

        elif choice == '6':  # Load from file
            inventory.load_from_file("inventory.json")
            print("Loaded!")

        elif choice == '7':  # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")
