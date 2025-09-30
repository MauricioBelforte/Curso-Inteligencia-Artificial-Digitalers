/* DESAFIO EJERCICIO 3: CONSULTAS EN SQL */
/* Se trabaja sobre esta base de datos https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all */

SELECT * FROM Customers WHERE City="Madrid";

SELECT ContactName, Address FROM Customers WHERE PostalCode="28034";

SELECT ContactName, City FROM Customers WHERE Country="Argentina";

SELECT ProductName FROM Products WHERE Price > 39;

SELECT * FROM Products WHERE Unit="24 - 4 oz tins";

SELECT ShipperName,Phone FROM Shippers;

SELECT OrderID,OrderDetailID FROM OrderDetails WHERE ProductID=42 ;