
"""
1. SELECT customer_id, SUM(amount) AS total_amount FROM orders GROUP BY customer_id;
2. SELECT customer_id, MAX(amount) AS max_amount FROM orders GROUP BY customer_id ORDER BY max_amount DESC LIMIT 1;
3. SELECT COUNT(id) AS max_orders_per_year FROM orders WHERE EXTRACT(YEAR FROM order_date) = 2023;
4. SELECT customer_id, ROUND(AVG(amount), 2) as avg_amount_per_customer FROM orders GROUP BY customer_id;
"""