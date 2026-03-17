# Simple Retail Store Database

This is a simple database project I created to practice my basic SQL skills. The idea is to build a basic retail store system to manage customers, products, and orders, and see how relational tables work together.

### How it works

The project creates a local database with three main tables:
* **Customers:** Stores basic customer information (ID, Name, City).
* **Products:** Stores product details (ID, Name, Price).
* **Orders:** Links customers to the products they bought using Foreign Keys.

I used Python to run the SQL commands so it can be easily executed in the terminal without needing to install a complex database server.

### Technologies Used

* SQL
* Python (sqlite3 library)

### How to Run

1. Download or clone the project file (`main.py`).
2. Open your terminal or VS Code.
3. Run the script by typing: `python main.py`
4. A local `retail_store.db` file will be created automatically, and the console will print the inserted data to show it works.

### What I Learned

Through this project, I improved my understanding of relational database design. I learned how to create tables, use Primary and Foreign Keys to link them, and how to execute basic SQL queries (CREATE, INSERT, SELECT) using Python.
