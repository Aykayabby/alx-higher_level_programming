-- A script that displays records from second_table with name in descending order.
SELECT score, name FROM second_table WHERE name is not NULL AND name!="" ORDER BY score DESC;
