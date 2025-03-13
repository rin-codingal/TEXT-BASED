CREATE TABLE IF NOT EXISTS STUDENTS (
  ROLL_NO TEXT PRIMARY KEY,
  SNAME TEXT NOT NULL,
  SADDRESS TEXT,
  PHONE TEXT,
  AGE INTEGER
);

-- Insert sample data into the STUDENT table
INSERT INTO STUDENTS (ROLL_NO, SNAME, SADDRESS, PHONE, AGE) VALUES
  ("1", "Andrew", "Jakarta", "+62-13452374345", 17),
  ("2", "Jack", "Surabaya", "+62-13452371298", 18),
  ("3", "Ashley", "Semarang", "+62-13452377432", 20),
  ("4", "Randy", "Palembang", "+62-79542374345", 18),
  ("5", "Jessica", "Kuta", "+62-13452398342", 20),
  ("6", "Abdul", "Surabaya", "+62-45622374747", 18);

-- Select all records from the Salesman table to verify insertion (if required)
SELECT * FROM Salesman;

-- Select all records from the STUDENTS table to verify insertion
SELECT * FROM STUDENTS;

-- Query students who are 18 years old and live in Surabaya
SELECT * FROM STUDENTS WHERE AGE = 18 AND SADDRESS = "Surabaya";

-- Query students who are 18 years old and named Jack
SELECT * FROM STUDENTS WHERE AGE = 18 AND SNAME = "Jack";

-- Query students named Jack or Randy
SELECT * FROM STUDENTS WHERE SNAME = "Jack" OR SNAME = "Randy";

-- Query students named Jack or aged 20
SELECT * FROM STUDENTS WHERE SNAME = "Jack" OR AGE = 20;

-- Query students aged 18 and named Jack or Abdul
SELECT * FROM STUDENTS WHERE AGE = 18 AND (SNAME = "Jack" OR SNAME = "Abdul");