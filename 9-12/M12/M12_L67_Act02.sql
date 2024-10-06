-- create table
CREATE TABLE IF NOT EXISTS Salesman (
  SalesID TEXT PRIMARY KEY,
  Sname TEXT,
  city TEXT,
  Comission REAL
);

-- insert the data
INSERT INTO Salesman (SalesID, Sname, city, Comission) VALUES
  ("7001", "Jessica Wong", "Berlin", 0.15),
  ("7002", "James White", "Paris", 0.17),
  ("7005", "Andrew Smith", "London", 0.11),
  ("7006", "Alex McGrager", "New York", 0.14),
  ("7007", "Paul Adam", "Singapore", 0.13),
  ("7003", "Tristan Alexander", "San Jose", 0.12);

-- displaying all the data of salesman
SELECT * FROM Salesman;

CREATE TABLE IF NOT EXISTS Orders (
  ordNum TEXT PRIMARY KEY,
  purch_amt REAL,
  ord_date TEXT,
  customer_id TEXT,
  Salesman_id TEXT
);

INSERT INTO Orders (ordNum, purch_amt, ord_date, customer_id, Salesman_id) VALUES
  ("90001", 150.5, "2024-10-05", "3005", "7002"),
  ("90002", 270.65, "2024-09-10", "3001", "7001"),
  ("90003", 65.26, "2024-10-05", "3002", "7003"),
  ("90004", 110.5, "2024-08-17", "3009", "7007"),
  ("90005", 948.5, "2024-09-10", "3005", "7005"),
  ("90006", 2400.6, "2024-07-27", "3007", "7006");

SELECT * FROM Orders;

-- displaying some of the data from table salesman
SELECT Sname, Comission FROM Salesman;
