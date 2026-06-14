CREATE TABLE IF NOT EXISTS DEPARTMENT (
  EMPLOYEE_ID TEXT PRIMARY KEY,
  EMPLOYEE_NAME TEXT,
  DEPARTMENT_ID TEXT,
  MANAGER_ID TEXT,
  SALARY REAL
);

INSERT INTO DEPARTMENT (EMPLOYEE_ID, EMPLOYEE_NAME, DEPARTMENT_ID, MANAGER_ID, SALARY) VALUES
  ("100", "Jessica Parker", "90", "100", 24000),
  ("101", "Nicole Braxton", "90", "100", 17000),
  ("102", "Andrew Lee", "90", "102", 9000),
  ("103", "Percy Jackson", "60", "103", 4800),
  ("104", "John Smith", "60", "103", 25000),
  ("105", "Vanessa Alexander", "50", "100", 4200),
  ("106", "Christopher Dan", "60", "102", 5000),
  ("107", "David Berg", "90", "100", 6000);

-- Query to count the number of employees in each department
SELECT department_id AS "Department Code", COUNT(*) AS "No of Employees" 
FROM DEPARTMENT
GROUP BY department_id; 

-- Query to sum the salary of each department
SELECT department_id, SUM(salary) 
FROM DEPARTMENT 
GROUP BY department_id;

-- Query to count the number of employees and sum the salary in each department
SELECT department_id AS "Department Code", COUNT(*) AS "No of Employees", SUM(salary) AS "Total Salary" 
FROM DEPARTMENT 
GROUP BY department_id; 

-- Query to sum the salary of employees with a specific manager
SELECT department_id AS "Department Code", SUM(salary) AS "Total Salary" 
FROM DEPARTMENT 
WHERE MANAGER_ID = "103" 
GROUP BY department_id;

-- Query to find departments with more than 2 employees
SELECT department_id, COUNT(*) AS "No. of Employees" 
FROM DEPARTMENT 
GROUP BY department_id 
HAVING COUNT(*) > 2;
