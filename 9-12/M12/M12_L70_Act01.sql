CREATE TABLE IF NOT EXISTS NOBEL_WIN (
    NOBEL_ID TEXT PRIMARY KEY,
    NOBEL_YEAR INTEGER,
    NOBEL_SUBJECT TEXT,
    WINNER TEXT,
    COUNTRY TEXT,
    CATEGORY TEXT
);

INSERT INTO NOBEL_WIN (NOBEL_ID, NOBEL_YEAR, NOBEL_SUBJECT, WINNER, COUNTRY, CATEGORY) VALUES
  ("N001", 1970, "Physics", "HANNES ALFVEN", "Sweden", "Scientist"),
  ("N002", 1970, "Physics", "LOUIS NEEL", "France", "Scientist"),
  ("N003", 1971, "Physics", "PAUL", "France", "Scientist"),
  ("N004", 1971, "Chemistry", "HAMILTON", "Sweden", "Linguist"),
  ("N005", 1972, "Literature", "BERNARD KELSON", "Germany", "Economist"),
  ("N006", 1972, "Economics", "JOSEPH", "Russia", "Economist"),
  ("N007", 1973, "Biology", "PHILIPS", "USA", "Prime Minister"),
  ("N008", 1980, "Biology", "MARTIN", "USA", "President"),
  ("N009", 1981, "Physiology", "HANNAH", "Hungary", "Scientist"),
  ("N010", 1975, "Physics", "PETER", "Chile", "Scientist");

-- Select all records from the NOBEL_WIN table where the NOBEL_SUBJECT does not start with "P"
SELECT * 
FROM NOBEL_WIN 
WHERE NOBEL_SUBJECT NOT LIKE "P%";

