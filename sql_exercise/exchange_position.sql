# Write your MySQL query statement below

SELECT (CASE WHEN s.id % 2 = 1 AND s.id != (SELECT COUNT(*) FROM seat) THEN s.id + 1
             WHEN s.id % 2 = 0 THEN s.id - 1
             ELSE s.id
             END) AS id, s.student
FROM seat s
ORDER BY id

