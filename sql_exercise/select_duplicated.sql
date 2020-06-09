# Write your MySQL query statement below
SELECT t1.Email
FROM
    (SELECT COUNT(p.Email) dup_count, p.Email
    FROM Person p
    GROUP BY p.Email) t1
WHERE dup_count >1