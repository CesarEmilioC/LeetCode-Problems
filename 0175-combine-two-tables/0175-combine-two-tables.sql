/*
Cesar Emilio Castaño Marin
Solution: Combine Two Tables
Github Username: CesarEmilioC
*/
# Write your MySQL query statement below
# We select the required fields for the output
SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM Person
# We take the inner join of them
INNER JOIN Address ON Person.personId = Address.personId
# We union this table with the one conformed by the persons that are not in the address table
UNION
SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM Person
LEFT JOIN Address ON Person.personId = Address.personId;



