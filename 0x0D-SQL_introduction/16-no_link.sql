-- script that lists all records for columns that only have a name
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
