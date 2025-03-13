CREATE TABLE IF NOT EXISTS Plants (
  Plants_ID TEXT PRIMARY KEY,
  Plants_Name TEXT,
  Category TEXT,
  Supplier_ID TEXT,
  Price INTEGER
);

INSERT INTO Plants (Plants_ID, Plants_Name, Category, Supplier_ID, Price) VALUES
("P001", "Rose", "Flower", "S001", 25000),
("P002", "Jasmine", "Flower", "S001", 15000),
("P003", "Sunflower", "Flower", "S001", 17000),
("P004", "Grape", "Fruit", "S002", 20000),
("P005", "Orange", "Fruit", "S002", 15000),
("P006", "Cherry", "Fruit", "S002", 16000),
("P007", "Rosemary", "Herbs", "S003", 15000);

select * from Plants;
-- Query to count the number of plants in each category
SELECT Category AS "Plant Category", COUNT(*) AS "No of Plants" 
FROM Plants
GROUP BY Category; 

-- Query to sum the price of each category
SELECT Category, SUM(Price) 
FROM Plants 
GROUP BY Category;

-- Query to count the number of plants and sum the price in each category
SELECT Category AS "Plant Category", COUNT(*) AS "No of Plants", SUM(Price) AS "Total Price" 
FROM Plants 
GROUP BY Category; 

-- Query to sum the price of plants with a specific supplier
SELECT Category AS "Plant Category", SUM(Price) AS "Total Price" 
FROM Plants 
WHERE Supplier_ID = "S001" 
GROUP BY Category;

-- Query to find plants category with more than 2 plants
SELECT Category, COUNT(*) AS "No. of Plants" 
FROM Plants 
GROUP BY Category 
HAVING COUNT(*) > 2;