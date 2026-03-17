import sqlite3


conn = sqlite3.connect('retail_store.db')
cursor = conn.cursor()


sql_commands = """
-- Create Customers Table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    City VARCHAR(50)
);

-- Create Products Table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Price DECIMAL(10, 2)
);

-- Create Orders Table 
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Insert sample data 
INSERT INTO Customers VALUES (1, 'Ahmed', 'Riyadh'), (2, 'Sarah', 'Jeddah'), (3, 'Mohammed', 'Jazan');
INSERT INTO Products VALUES (101, 'Laptop', 3500.00), (102, 'Bluetooth Headphones', 150.00), (103, 'Wireless Mouse', 50.00);
INSERT INTO Orders VALUES (1001, 1, 101, 1, '2026-03-17'), (1002, 2, 102, 2, '2026-03-16'), (1003, 3, 103, 1, '2026-03-17');
"""


cursor.executescript(sql_commands)


cursor.execute("SELECT * FROM Customers;")
print("Customers in Database:")
for row in cursor.fetchall():
    print(row)


conn.commit()
conn.close()

print("\nDatabase created successfully!")