CREATE TABLE IF NOT EXISTS Salesperson (
  Salesperson_id TEXT PRIMARY KEY,
  name TEXT,
  city TEXT,
  Comission REAL
);

INSERT INTO Salesperson (Salesperson_id, name, city, Comission) VALUES
    ("7001", "Jessica Wong", "Berlin", 0.18),
    ("7002", "James White", "Paris", 0.17),
    ("7003", "Andrew Smith", "London", 0.17),
    ("7004", "Alex McGrager", "New York", 0.18),
    ("7005", "Paul Adam", "Copenhagen", 0.17),
    ("7006", "Tristan Alexander", "Moscow", 0.11);

CREATE TABLE IF NOT EXISTS Cust (
  customer_id TEXT,
  cust_name TEXT PRIMARY KEY,
  city TEXT,
  grade INTEGER,
  Salesperson_id TEXT,
  FOREIGN KEY (Salesperson_id) REFERENCES Salesperson(Salesperson_id)
);

INSERT INTO Cust (customer_id, cust_name, city, grade, Salesperson_id) VALUES
  ("C1001", "Jay Idzes", "New York", 100, "7004"),
  ("C1002", "Justin Hubner", "London", 300, "7003"),
  ("C1003", "Sandy Walsh", "Moscow", 200, "7006"),
  ("C1004", "Garaga", "Paris", NULL, "7002"),
  ("C1005", "Zoe Saldana", "California", 200, "7004"),
  ("C1006", "Towel Toyyib", "London", NULL, "7003"),
  ("C1007", "Bradd Pitt", "Copenhagen", 200, "7005"),  
  ("C1008", "Andrew Smith", "London", 300, "7003"),  
  ("C1009", "Ragnar Oeratmangoen", "Berlin", 100, "7001");

-- Create the Orders table if it does not exist
CREATE TABLE IF NOT EXISTS MyOrders (
  ord_no TEXT PRIMARY KEY,
  purch_amt REAL,
  ord_date TEXT,
  customer_id TEXT,
  Salesperson_id TEXT,
  FOREIGN KEY (customer_id) REFERENCES Cust(customer_id),
  FOREIGN KEY (Salesperson_id) REFERENCES Salesperson(Salesperson_id)
);

-- Insert sample data into the Orders table
INSERT INTO MyOrders (ord_no, purch_amt, ord_date, customer_id, Salesperson_id) VALUES
  ("P30001", 175.5, "2024-10-05", "C1005", "7002"),
  ("P30002", 375.65, "2024-09-10", "C1001", "7001"),
  ("P30003", 55.26, "2024-10-05", "C1002", "7003"),
  ("P30004", 210.5, "2024-08-17", "C1009", "7007"),
  ("P30005", 849.5, "2024-09-10", "C1005", "7005"),
  ("P30006", 2700.6, "2024-07-27", "C1007", "7006");



-- Matching customers and salesmen by city
SELECT Cust.cust_name, Salesperson.name, Salesperson.city
FROM Cust
JOIN Salesperson ON Cust.city = Salesperson.city;

-- Linking customers to their salesmen
SELECT Cust.cust_name, Salesperson.name
FROM Cust
JOIN Salesperson ON Cust.Salesperson_id = Salesperson.Salesperson_id;

-- Fetching orders where customer"s city does not match Salesperson"s city
SELECT MyOrders.ord_no, Cust.cust_name, MyOrders.customer_id, MyOrders.Salesperson_id
FROM MyOrders
JOIN Cust ON MyOrders.customer_id = Cust.customer_id
JOIN Salesperson ON MyOrders.Salesperson_id = Salesperson.Salesperson_id
WHERE Cust.city <> Salesperson.city;

-- Fetching all orders with customer names
SELECT MyOrders.ord_no, Cust.cust_name
FROM MyOrders
JOIN Cust ON MyOrders.customer_id = Cust.customer_id;

-- Customers with grades
SELECT Cust.cust_name AS "Customer", Cust.grade AS "Grade"
FROM MyOrders
JOIN Salesperson ON MyOrders.Salesperson_id = Salesperson.Salesperson_id
JOIN Cust ON MyOrders.customer_id = Cust.customer_id
WHERE Cust.grade IS NOT NULL;

-- Customers with salesmen where commission is between 0.12 and 0.14
SELECT Cust.cust_name AS "Customer", Cust.city AS "City", Salesperson.name AS "Salesperson", Salesperson.Comission
FROM Cust
JOIN Salesperson ON Cust.Salesperson_id = Salesperson.Salesperson_id
WHERE Salesperson.Comission BETWEEN 0.12 AND 0.14;

-- Calculating commissions for orders where customer grade is 200 or more
SELECT MyOrders.ord_no AS "Order Number", Cust.cust_name AS "Customer Name", Salesperson.Comission AS "Commission %", 
      MyOrders.purch_amt * Salesperson.Comission AS "Commission"
FROM MyOrders
JOIN Salesperson ON MyOrders.Salesperson_id = Salesperson.Salesperson_id
JOIN Cust ON MyOrders.customer_id = Cust.customer_id
WHERE Cust.grade >= 200;

-- Orders on a specific date
SELECT *
FROM Cust
JOIN MyOrders ON Cust.customer_id = MyOrders.customer_id
WHERE MyOrders.ord_date = "2024-10-05";

