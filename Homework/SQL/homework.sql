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

#select * from film;
#select * from language;

SELECT title
FROM film
WHERE 
	(
	title like 'K%' OR 
    title like 'Q%'
    )
    
    AND
    
    language_id IN (
		SELECT language_id
		FROM language
		WHERE name = 'English' 
		)
;

#7b
SELECT
	concat(first_name, " ", last_name) as "Actor Name"
FROM actor
WHERE actor_id IN (
	SELECT actor_id
    FROM film_actor
    WHERE film_id IN (
		SELECT film_id
        FROM film
        WHERE title = 'Alone Trip'
        )
	)
;

#7c
SELECT
	customer.first_name,
    customer.last_name
FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
JOIN country ON city.country_id = country.country_id
WHERE country.country = 'Canada'
;

#7d
/*select * from category;
select * from film;*/

SELECT film.title
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Family'
;

#7e
#select * from film;
#select * from rental;

SELECT title
FROM film
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
GROUP BY title
ORDER BY COUNT(title) desc
;

#7f
SELECT
	store.store_id,
    SUM(payment.amount) as 'Total Business (USD)'
FROM store
JOIN inventory ON store.store_id = inventory.store_id
JOIN rental ON rental.inventory_id = inventory.inventory_id
JOIN film ON film.film_id = inventory.film_id
JOIN payment ON payment.rental_id = rental.rental_id
GROUP BY store_id
;

#7g
SELECT
	store.store_id,
    city.city,
    country.country
FROM store
JOIN address ON store.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
JOIN country ON city.country_id = country.country_id
;

#7h
SELECT
	category.name as 'Genre',
    SUM(payment.amount) as 'Gross Revenue'
FROM category
JOIN film_category ON category.category_id = film_category.category_id
JOIN inventory ON film_category.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
JOIN payment ON rental.rental_id = payment.rental_id
GROUP by category.name
ORDER BY SUM(payment.amount) DESC LIMIT 5
;

#8
#8a
CREATE VIEW top_five_genres AS

SELECT
	category.name as 'Genre',
    SUM(payment.amount) as 'Gross Revenue'
FROM category
JOIN film_category ON category.category_id = film_category.category_id
JOIN inventory ON film_category.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
JOIN payment ON rental.rental_id = payment.rental_id
GROUP by category.name
ORDER BY SUM(payment.amount) DESC LIMIT 5
;

#8b
SELECT * from top_five_genres;

#8c
DROP VIEW top_five_genres;








	



 










