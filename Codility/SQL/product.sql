/*
For each pair of city and product, return the names of the city and product as well as the total amount spent on the product to 2dp. order the result by the amount spent from high to low then by city name and product name in ascending order.

Tables:
City - id, name, postal code, countryid
customer - id, customer_name, city_id, customer-address, contact_person, email, phone, isactive
invoice - id, invoice_number, customer_id, user_account_id, total_price

invoice_item - id, invoice_id, product_id, quantity, price, line_total_price
product - id, sku,product_name,product_description,current_price,quantity_in_stock,isactive

*/ 
SELECT 
    c.city_name AS name,
    p.product_name,
    ROUND(SUM(ii.quantity * ii.price), 2) AS total_amount_spent
FROM 
    City c
INNER JOIN 
    customer cust ON c.id = cust.city_id
INNER JOIN 
    invoice inv ON cust.id = inv.customer_id
INNER JOIN 
    invoice_item ii ON inv.id = ii.invoice_id
INNER JOIN 
    product p ON ii.product_id = p.id
GROUP BY 
    c.city_name, p.product_name
ORDER BY 
    total_amount_spent DESC, c.city_name ASC, p.product_name ASC;
