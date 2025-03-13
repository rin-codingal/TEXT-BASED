CREATE TABLE IF NOT EXISTS FLOWERS(
  PRO_ID TEXT PRIMARY KEY,
  PRO_NAME TEXT,
  PRO_PRICE INTEGER,
  PRO_COM TEXT
);

INSERT INTO FLOWERS(PRO_ID,PRO_NAME,PRO_PRICE,PRO_COM) VALUES
  ("101","Rose",2700,"15"),
  ("102","Jasmine",350,"16"),
  ("103","Waterlily",500,"14"),
  ("104","Sunflower",750,"16"),
  ("105","Strawflower",5000,"11"),
  ("106","Calendula",4500,"12"),
  ("107","Marigold",700,"12"),
  ("108","Aster",2500,"13");

-- displaying data with minimum price
SELECT PRO_NAME, PRO_PRICE FROM FLOWERS WHERE PRO_PRICE = (SELECT MIN(PRO_PRICE) FROM PRODUCT);

-- displaying data with maximum price
select PRO_NAME, PRO_PRICE FROM FLOWERS WHERE PRO_PRICE =  (SELECT MAX(PRO_PRICE) FROM PRODUCT);    

-- displaying data with specified pattern
SELECT PRO_NAME, PRO_PRICE FROM FLOWERS WHERE PRO_NAME LIKE "%flower";

