-- A script that groups the score in second_table
-- it also counts it and labels the count as number 
SELECT score, COUNT( * ) as number FROM second_table GROUP BY score ORDER BY number DESC;
