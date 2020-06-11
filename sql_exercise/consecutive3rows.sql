# Write your MySQL query statement below
SELECT t1.id, t1.visit_date, t1.people
FROM
    (SELECT LEAD(s.people, 1) OVER (ORDER BY s.visit_date) the_former_1,
            LEAD(s.people, 2) OVER (ORDER BY s.visit_date) the_former_2,
            LAG(s.people, 1) OVER (ORDER BY s.visit_date)  the_latter_1,
            LAG(s.people, 2) OVER (ORDER BY s.visit_date)  the_latter_2,
           s.id, s.visit_date, s.people
    FROM stadium s) t1
WHERE t1.people >= 100 AND t1.the_former_1 >= 100 AND t1.the_former_2 >= 100
        OR
      t1.people >= 100 AND t1.the_latter_1 >= 100 AND t1.the_latter_2 >= 100
        OR
      t1.people >= 100 AND t1.the_latter_1 >= 100 AND t1.the_former_1 >= 100