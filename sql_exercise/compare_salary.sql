# Write your MySQL query statement below
SELECT t1.Employee
FROM
    (SELECT e.Name Employee, e.salary employee_salary, e1.Name manager, e1.Salary manager_salary
    FROM Employee e
    LEFT JOIN Employee e1
    ON e.ManagerId = e1.Id) t1
WHERE t1.employee_salary > t1.manager_salary