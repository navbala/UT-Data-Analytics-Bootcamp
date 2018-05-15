# Naveen's SQL HW

## Use the sakila db

```sql
USE sakila;
```

## 1a - Display the first and last names of all actors from the table actor.

```sql
SELECT
   first_name as `First Name`,
   last_name as `Last Name`
FROM actor;
```

## 1b - Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.

```sql
SELECT concat(`first_name`, " ", `last_name`) as `Full Name`
FROM actor;
```

## 2a - You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?

```sql
SELECT
   actor_id,
   first_name,
   last_name
FROM
   actor
WHERE
   first_name = "Joe"
;
```

## 2b - Find all actors whose last name contain the letters GEN:

```sql
SELECT
   first_name,
   last_name
FROM actor
WHERE
   last_name LIKE '%GEN%'
;
```

## 2c - Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:

```sql
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
```

## 2d - Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:

 ```sql
SELECT
   country_id,
   country
FROM
   country
WHERE
   country IN ('Afghanistan', 'Bangladesh', 'China')
;
```


## 3a - Add a middle_name column to the table actor. Position it between first_name and last_name. Hint: you will need to specify the data type.

```sql
ALTER TABLE actor
ADD COLUMN middle_name varchar(20) AFTER first_name;
```

## 3b - You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to blobs.

```sql
ALTER TABLE actor MODIFY middle_name blobs;
```

## 3c - Now delete the middle_name column.

```sql
ALTER TABLE actor DROP COLUMN middle_name;
```


## 4a - List the last names of actors, as well as how many actors have that last name.

```sql
SELECT
   last_name,
   count(*) as `Frequency`
FROM
   actor
GROUP BY
   last_name
;
```

## 4b - List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors

```sql
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
```

## 4c - Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS, the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.

```sql
UPDATE
   actor
SET
   first_name = "HARPO"
WHERE
   first_name = "Harpo" and
   last_name = "Williams"
;
 ```

## 4d - Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO. Otherwise, change the first name to MUCHO GROUCHO, as that is exactly what the actor will be with the grievous error. BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO, HOWEVER! (Hint: update the record using a unique identifier.)

```sql
UPDATE
   actor
SET
   first_name = "GROUCHO"
WHERE
   actor_id = 172
;
```


## 5a - You cannot locate the schema of the address table. Which query would you use to re-create it?

```sql
SHOW CREATE TABLE address;
```


## 6a - Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:

```sql
SELECT
   staff.first_name,
   staff.last_name,
   address.address
FROM staff
JOIN address
ON
   staff.address_id = address.address_id
;
```

## 6b - Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.

```sql
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
```

## 6c - List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.

```sql
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
```

## 6d - How many copies of the film Hunchback Impossible exist in the inventory system?

```sql
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
```

## 6e - Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:

```sql
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
```

## 7a - The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q have also soared in popularity. Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.

```sql
SELECT title
FROM film
WHERE (
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
```

## 7b - Use subqueries to display all actors who appear in the film Alone Trip.

```sql
SELECT
   concat(first_name, " ", last_name) as 'Actor Name'
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
```

## 7c - You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.

```sql
SELECT
   customer.first_name,
   customer.last_name
FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
JOIN country ON city.country_id = country.country_id
WHERE country.country = 'Canada'
;
```

## 7d - Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as family films.

```sql
SELECT film.title
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Family'
;
```

## 7e - Display the most frequently rented movies in descending order.

```sql
SELECT title
FROM film
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
GROUP BY title
ORDER BY COUNT(title) desc
;
```

## 7f - Write a query to display how much business, in dollars, each store brought in.

```sql
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
```

## 7g - Write a query to display for each store its store ID, city, and country.

```sql
SELECT
   store.store_id,
   city.city,
   country.country
FROM store
JOIN address ON store.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
JOIN country ON city.country_id = country.country_id
;
```

## 7h - List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)

```sql
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
```


## 8a - In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.

```sql
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
```

## 8b - How would you display the view that you created in 8a?

```sql
SELECT * from top_five_genres;

```

## 8c - You find that you no longer need the view top_five_genres. Write a query to delete it.

```sql
DROP VIEW top_five_genres;
```
