-- Number by score
-- lists the number of records with the same score
SELECT score, COUNT(score) AS number FROM second_table
    GROUP BY score
    ORDER BY score DESC;
