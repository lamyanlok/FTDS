use sakila;

-- ## 1. Count how many actors there are for the movie 'HAUNTING PIANIST'
select count(*) from film_actor 
where film_id = (select film_id from film where title = 'HAUNTING PIANIST');

-- ## 2. Count how many Mandarin movies there are for each store
select count(language_id),store_id from inventory inner join film 
on inventory.film_id = film.film_id 
where language_id = (select language_id from language where name = 'English') 
group by store_id;

-- ## 3.Return the names of the customers who has spent more than 20 dollars from rentals
select first_name, last_name from customer 
where customer_id = 
(select customer_id from payment group by customer_id order by sum(amount) desc limit 1);

-- ## 4.Return the count of 'PARK CITIZEN' movies in the inventory.
select count(*) from inventory where film_id = 
(select film_id from film where title = 'PARK CITIZEN');

-- ## 5. Count how many rentals there are for the movie 'CHICKEN HELLFIGHTERS'.
select count(*) from rental where inventory_id in 
(select inventory_id from inventory where film_id = 
(select film_id from film where title = 'CHICKEN HELLFIGHTERS'));

-- ## 6.Count how many customers there are from the 'Sichuan' district
select count(*) from customer where address_id in 
(select address_id from address where district = 'Sichuan');

-- ## 7.Return the country with the postal code 49757.
select country from country where country_id = 
(select country_id from city where city_id = 
(select city_id from address where postal_code = 49757));

-- ## 8.Count how many movies of category 'Comedy' are in the store with id = 2.
select count(*) from inventory where store_id = 2 and 
film_id in(select film_id from film_category where category_id = 
(select category_id from category where name = 'Comedy'));

-- ## 9.Return the names of the movies that BURT DUKAKIS has been in.
select title from film where film_id in 
(select film_id from film_actor where actor_id = 
(select actor_id from actor where first_name='BURT' and last_name='DUKAKIS'));

-- ## 10.Return the names of the movies that have the rating 'PG' that are in the store with id = 1
select title from film where rating = 'PG' and film_id in
(select film_id from inventory where store_id = 1);