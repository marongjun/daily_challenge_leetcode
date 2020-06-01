# Write your MySQL query statement below
SELECT t1.class
FROM
(SELECT COUNT(DISTINCT(c.student)) AS stu_num, c.class
FROM courses c
GROUP BY class) t1
WHERE t1.stu_num >= 5;