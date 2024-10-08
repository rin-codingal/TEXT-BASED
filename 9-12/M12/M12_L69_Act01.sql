CREATE TABLE IF NOT EXISTS Grocery_Product (
  PRODUCT_ID TEXT PRIMARY KEY,
  PRODUCT_NAME TEXT,
  SUPPLIER_ID TEXT,
  CATEGORY_ID TEXT,
  UNIT TEXT,
  PRICE REAL
);

INSERT INTO Grocery_Product (PRODUCT_ID, PRODUCT_NAME, SUPPLIER_ID, CATEGORY_ID, UNIT, PRICE) VALUES
  ("P001", "Tea", "S001", "C01", "10 BOXES*20 BAGS", 35),
  ("P002", "Ketchup", "S001", "C01", "24-12 OZ BOTTLES", 25),
  ("P003", "Maple syrup", "S001", "C02", "12-550 ML BOTTLES", 17),
  ("P004", "Cucumber pickle", "S002", "C02", "48- 6 OZ JARS", 23),
  ("P005", "Tisane", "S002", "C02", "36 BOXES", 25.7);

-- Query to count the number of Grocery_Product
SELECT COUNT(PRODUCT_ID) AS Product_Count FROM Grocery_Product;

-- Query to find the average price of Grocery_Product
SELECT AVG(PRICE) AS Average_Price FROM Grocery_Product;

-- Query to find the total price of Grocery_Product
SELECT SUM(PRICE) AS Total_Price FROM Grocery_Product;