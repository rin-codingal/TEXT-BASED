CREATE TABLE IF NOT EXISTS drinks (
  PRODUCT_ID TEXT PRIMARY KEY,
  PRODUCT_NAME TEXT,
  SUPPLIER_ID TEXT,
  UNIT TEXT,
  PRICE REAL
);

INSERT INTO drinks (PRODUCT_ID, PRODUCT_NAME, SUPPLIER_ID, UNIT, PRICE) VALUES
  ("P001", "Tea", "S001", "450 ml bottles", 20),
  ("P002", "Coffee", "S001", "250 ml bottles", 30),
  ("P003", "Orange Juice", "S001", "300 ml bottles", 17),
  ("P004", "Water", "S002", "600 ml bottles", 15),
  ("P005", "Milk", "S002", "1000 ml bottles", 35.7);

-- Query to count the number of drinks
SELECT COUNT(PRODUCT_ID) AS Product_Count FROM drinks;

-- Query to find the average price of drinks
SELECT AVG(PRICE) AS Average_Price FROM drinks;

-- Query to find the total price of drinks
SELECT SUM(PRICE) AS Total_Price FROM drinks;