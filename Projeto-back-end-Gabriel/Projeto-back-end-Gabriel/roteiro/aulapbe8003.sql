--SQlite
CREATE TABLE Persons(
   PersonID INT,
    LastName VARCHAR (255),
    FristName VARCHAR (255),
    Address VARCHAR(255),
    City VARCHAR(255)
);

--INSERT INTO Persons (PersonID, LastName, FristName)
--VALUES (100, "Value1", "value2", "value3");

--SELECT LastName
--FROM Persons
--WHERE LastName = "Gabriel"

INSERT INTO Persons (PersonID, LastName, FristName, Address, City)
VALUES(200, "Victor","Rodrigues","Rua x", "Rio de janeiro");

INSERT INTO Persons (PersonID, LastName, FristName, Address, City)
VALUES (200,"Victor", "Rodrigues", "Rua x", "Rio de janeiro");


UPDATE Persons
SET LastName = "Carlinhos", FristName = "dalva"
WHERE PersonID = 100;

DELETE FROM Persons WHERE = 200;