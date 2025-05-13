# 🛒 Inventory Management System (Using Python OOP)

This is a beginner-to-intermediate Python project where you manage products like **Electronics, Groceries, and Clothing** using **Object-Oriented Programming (OOP)** concepts. The system lets you **add**, **sell**, **search**, **save**, and **load** your inventory easily through a simple CLI menu.

---

## 🚀 Features

* Add new products (Electronics, Grocery, Clothing)
* Sell products (with stock validation)
* Search products by name
* List all products
* Save inventory to a JSON file
* Load inventory from a JSON file
* Handles errors like out-of-stock or duplicate products

---

## 🐍 OOP Concepts Covered

* **Classes & Objects**
* **Inheritance**
* **Encapsulation**
* **Polymorphism (Method overriding)**
* **Abstract Base Classes**
* **Custom Exceptions**
* **File Handling (JSON Save/Load)**

---

## 📦 Product Types

| Type        | Extra Attributes                 |
| ----------- | -------------------------------- |
| Electronics | `brand`, `warranty (years)`      |
| Grocery     | `expiry_date` + checks expired ✅ |
| Clothing    | `size`, `material`               |

---

## 📂 Project Structure

```
inventory_management/
│
├── inventory.py  # Main system code
├── inventory.json  # (Saved data file)
└── README.md
```

---

## 🛠️ How to Run

1. ✅ Make sure you have Python **3.10 or above** installed.
2. 📥 No external packages are needed (uses only built-in modules).
3. Open terminal/cmd and run:

```bash
python inventory.py
```

That’s it! You'll see the menu:

```
===== Inventory Menu =====
1. Add Product
2. Sell Product
3. List Products
4. Search Product
5. Save Inventory
6. Load Inventory
7. Exit
```

---

## 🔥 Example Actions

* Add an **Electronic product** with brand & warranty
* Add a **Grocery item** with an expiry date
* Add a **Clothing item** with size and material
* Sell stock (it prevents overselling)
* Save or load your products anytime!

---

## 💪 Learning Goals

* Practice **real-world** OOP design
* Understand **abstract classes** and **method overriding**
* Implement **error handling** and **data persistence**
* Gain confidence with **file operations** using JSON

---

## 📚 Requirements

* Python 3.10+
* No extra packages required (uses `abc`, `json`, `datetime`)

---

## ✨ Extra Challenges (Optional)

* Add more product types (e.g., Furniture 📦)
* Add feature to **remove expired groceries**
* Implement an option to **delete a product**
* Turn this CLI system into a **GUI** using Tkinter or Streamlit

---

