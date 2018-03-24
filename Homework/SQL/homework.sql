USE sakila;

#1
#select * from actor;

#1a
SELECT
	first_name as `First Name`,
    last_name as `Last Name`
FROM actor;

#1b
SELECT concat(`first_name`, " ", `last_name`) as `Full Name`
FROM actor;

#2
#2a
SELECT
	actor_id,
    first_name,
    last_name
FROM
	actor
WHERE
	first_name = "Joe"
;
    
#2b
SELECT
	first_name,
    last_name
FROM actor
WHERE
	last_name LIKE '%GEN%'
;

#2c
SELECT
    last_name,
    first_name
FROM actor
WHERE
	last_name LIKE '%LI%'
ORDER BY
	last_name,
    first_name
;

#2d
SELECT
	country_id,
    country
FROM
	country
WHERE
	country IN ('Afghanistan', 'Bangladesh', 'China')
;

#3
#3a
#SELECT DATA_TYPE 
#FROM INFORMATION_SCHEMA.COLUMNS
#WHERE 
#     TABLE_NAME = 'actor' AND 
#     COLUMN_NAME = 'first_name'
#;
 
ALTER TABLE actor
ADD COLUMN middle_name varchar(20) AFTER first_name;

#select * from actor;

#3b
ALTER TABLE actor MODIFY middle_name blob;

#3c
ALTER TABLE actor DROP COLUMN middle_name;

#select * from actor;

#4
#4a
SELECT
	last_name,
    count(*) as `Frequency`
FROM
	actor
GROUP BY
	last_name
;

#4b
SELECT
	last_name,
    count(*) as `Frequency`
FROM
	actor
GROUP BY
	last_name
HAVING
	Frequency >= 2
;

#4c
#select * from actor where first_name = "groucho";

UPDATE
	actor
SET
	first_name = "HARPO"
WHERE
	first_name = "Harpo" and
    last_name = "Williams"
;

#4d
UPDATE
	actor
SET
	first_name = "GROUCHO"
WHERE
	actor_id = 172
;

#5
#5a
SHOW CREATE TABLE address;

#6
#6a
SELECT
	staff.first_name,
    staff.last_name,
    address.address
FROM staff
JOIN address
ON
	staff.address_id = address.address_id
;

#6b
SELECT
	staff.first_name,
    staff.last_name,
    SUM(payment.amount) as `total amount`
FROM staff
JOIN payment
ON
	staff.staff_id = payment.staff_id
GROUP BY
	staff.staff_id
;

#6c
SELECT
	film.title,
    COUNT(film_actor.actor_id)
FROM film_actor
INNER JOIN film
ON
	film_actor.film_id = film.film_id
GROUP BY 
	film_actor.film_id
;

#6d
SELECT
	COUNT(film_id) as `film count`
FROM
	inventory
WHERE film_id in (
	SELECT
		film_id
	FROM
		film
	WHERE
		title = "Hunchback Impossible"
	)
;

#6e
SELECT
	concat(customer.first_name, " ", customer.last_name) as `Customer Name`,
    sum(payment.amount) as `Total Amount Paid`
FROM customer
JOIN payment
ON customer.customer_id = payment.customer_id
GROUP BY
	customer.customer_id
ORDER BY
	customer.last_name asc
;

#7
#7a

 










