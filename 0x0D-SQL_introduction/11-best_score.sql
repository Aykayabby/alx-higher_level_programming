-- A script that lists all the recoreds with a score >= 10 in second_table
-- 	both score and name should be displayed
-- 	score should be in descending order
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;