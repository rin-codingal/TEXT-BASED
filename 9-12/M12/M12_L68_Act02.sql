CREATE TABLE IF NOT EXISTS PRODUCT(
  PRO_ID TEXT PRIMARY KEY,
  PRO_NAME TEXT,
  PRO_PRICE INTEGER,
  PRO_COM TEXT
);

INSERT INTO PRODUCT(PRO_ID,PRO_NAME,PRO_PRICE,PRO_COM) VALUES
  ("101","Rose",2700,"15"),
  ("102","Jasmine",350,"16"),
  ("103","Waterlily",500,"14"),
  ("104","Sunflower",750,"16"),
  ("105","Strawflower",5000,"11"),
  ("106","Calendula",4500,"12"),
  ("107","Marigold",700,"12"),
  ("108","Aster",2500,"13");

SELECT PRO_NAME, PRO_PRICE
   FROM PRODUCT
   WHERE PRO_PRICE = 
    (SELECT MIN(PRO_PRICE) FROM PRODUCT);

SELECT PRO_NAME, PRO_PRICE
   FROM PRODUCT
   WHERE PRO_PRICE = 
    (SELECT MAX(PRO_PRICE) FROM PRODUCT);    

