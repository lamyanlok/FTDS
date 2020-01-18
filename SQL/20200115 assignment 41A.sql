-- Download the world database SQL script here: MySQL world database

-- 1.Return the country names that have English as their official language.
select country.name from country where country.Code in 
(select CountryCode from countrylanguage where language = 'English');

-- 2.Count how many countries there are in the Antarctica region.
select count(*) from country where region = 'Antarctica';

-- 3.Return the top 5 cities with the most population.
select name, Population from country order by population desc limit 5;

-- 4.Return the top 10 countries with the least life expectancy.
select name, lifeexpectancy from country order by lifeexpectancy asc limit 10;

-- 5.Return the top 5 districts with the most population.
select district, population from city order by population desc limit 5;

-- 6.Return the languages that have 50% or more of the population speak it in their respective countries.
select countrycode,language from countrylanguage where percentage > 50;

-- 7.Return the region with the highest average GNP.
select sum(GNP), region from country group by region order by sum(GNP) desc limit 1;

-- 8.Return the continent with the highest population density. (Hint: Population density = population/surface area)
select sum(population)/ sum(surfacearea),sum(population), sum(surfacearea), continent from country group by continent order by sum(population)/ sum(surfacearea) desc limit 1;

-- 9.Count how many countries speak French. 
select count(*) from countrylanguage where language = 'French';

-- 10.Return the countries which have their year of independence at 1950 or later.
select indepyear, name from country where indepyear < 1950 order by indepyear;