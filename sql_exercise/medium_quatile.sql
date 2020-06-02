USE pdd;

SELECT
@rowindex_max := COUNT(*) + 1
FROM orders;

WITH t1 AS (SELECT
ROW_NUMBER() OVER (ORDER BY o.order_pay) row_num,
o.order_pay
FROM orders o)

SELECT
AVG(t1.order_pay) AS median
FROM t1
WHERE t1.row_num IN (FLOOR(@rowindex_max/2), CEILING(@rowindex_max/2));

