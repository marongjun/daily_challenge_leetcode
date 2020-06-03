# Write your MySQL query statement below

SELECT t2.Department,t2.Employee, t2.Salary
FROM
(SELECT DENSE_RANK() OVER (PARTITION BY t1.Department ORDER BY t1.Salary DESC) dense_rank_index,
t1.Department,t1.Employee, t1.Salary
FROM
(SELECT d.name Department, e.Name Employee, e.Salary
FROM
Employee e
LEFT JOIN Department d
ON e.DepartmentId = d.Id) t1
WHERE t1.Department IS NOT NULL) t2
WHERE t2.dense_rank_index = 1
