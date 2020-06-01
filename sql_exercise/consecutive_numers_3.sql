# Write your MySQL query statement below
SELECT DISTINCT(t1.now_num) ConsecutiveNums
FROM
(SELECT
l.Num now_num,
LAG (l.Num) OVER (ORDER BY l.Id) pre_num,
LEAD(l.Num) OVER (ORDER BY l.Id) next_num
FROM logs l) t1
WHERE t1.pre_num = t1.now_num AND t1.now_num = t1.next_num;
