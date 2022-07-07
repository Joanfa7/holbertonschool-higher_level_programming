-- list all of a list
-- dont list rows
SELECT score, name FROM second_table WHERE name != '' AND name IS NOT NULL
ORDER BY score DESC;
