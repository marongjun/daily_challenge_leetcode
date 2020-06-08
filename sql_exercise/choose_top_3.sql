# Write your MySQL query statement below
SELECT t1.Department,t1.Employee,t1.Salary
FROM(
    SELECT DENSE_RANK() OVER (PARTITION BY e.DepartmentId ORDER BY Salary) rank_num,
        d.Name AS Department,
        e.Name AS Employee,
        e.Salary
    FROM Employee e LEFT JOIN Department d ON e.DepartmentId = d.Id) t1
WHERE rank_num <= 3;