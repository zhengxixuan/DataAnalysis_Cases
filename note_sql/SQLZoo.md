# SQLZoo

SQL exercises from [sqlzoo.net](https://sqlzoo.net/).

## Index

1. [SELECT Basics](https://sqlzoo.net/wiki/SELECT_basics)
2. [SELECT From World](https://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial)
3. [SELECT From Nobel](https://sqlzoo.net/wiki/SELECT_from_Nobel_Tutorial)
4. [SELECT in SELECT](https://sqlzoo.net/wiki/SELECT_within_SELECT_Tutorial)
5. [SUM and COUNT]()
6. [JOIN]()
7. [More JOIN]()
8. [Using NULL]()
9. [Self JOIN]()

## 01. SELECT Basics

1. Show the population of Germany.

```mysql
SELECT population
  FROM world
 WHERE name = 'Germany';
```

2. Show the name and the population for 'Sweden', 'Norway' and 'Denmark'.

```mysql
SELECT name, population
  FROM world
 WHERE name IN ('Sweden', 'Norway', 'Denmark');
```

3. Show the country and the area for countries with an area between 200,000 and 250,000.

```mysql
SELECT name, area
  FROM world
 WHERE area BETWEEN 200000 AND 250000;
```

## 02. SELECT From World

1. show the name, continent and population of all countries.

```mysql
SELECT name, continent, population
  FROM world;
```

2. Show the name for the countries that have a population of at least 200 million. 200 million is 200000000, there are eight zeros.

```mysql
SELECT name
  FROM world
 WHERE population >= 200000000;
```

3. Give the name and the per capita GDP for those countries with a population of at least 200 million.

```mysql
SELECT name, gdp/population
  FROM world
 WHERE population >= 200000000;
```

4. Show the name and population in millions for the countries of the continent 'South America'. Divide the population by 1000000 to get population in millions.

```mysql
SELECT name, population/1000000
  FROM world
 WHERE continent = 'South America';
```

5. Show the name and population for France, Germany, Italy.

```mysql
SELECT name, population
  FROM world
 WHERE name IN ('France', 'Germany', 'Italy');
```

6. Show the countries which have a name that includes the word 'United'.

```mysql
SELECT name
  FROM world
 WHERE name LIKE '%United%';
```

7. Show the countries that are big by area or big by population. Show name, population and area.

```mysql
SELECT name, population, area
  FROM world
 WHERE area > 3000000
    OR population > 250000000;
```

8. Show the countries that are big by area or big by population but not both. Show name, population and area.

```mysql
SELECT name, population, area
  FROM world
 WHERE area > 3000000
   XOR population > 250000000;
```

```mysql
SELECT name, population, area
  FROM world
 WHERE (area > 3000000 AND population < 250000000)
    OR (area < 3000000 AND population > 250000000)
```

9. For South America show population in millions and GDP in billions both to 2 decimal places.

```mysql
SELECT name, ROUND(population/1000000, 2), ROUND(gdp/1000000000, 2)
  FROM world
 WHERE continent = 'South America';
```

10. Show per-capita GDP for the trillion dollar countries to the nearest $1000.

```mysql
SELECT name, ROUND(gdp/population, -3)
  FROM world
 WHERE gdp > 1000000000000;
```

11. Show the name and capital where the name and the capital have the same number of characters.

```mysql
SELECT name, capital
  FROM world
 WHERE LENGTH(name) = LENGTH(capital);
```

12. Show the name and the capital where the first letters of each match. Don't include countries where the name and the capital are the same word.

```mysql
SELECT name, capital
  FROM world
 WHERE LEFT(name, 1) = LEFT(capital, 1)
   AND name <> capital;
```

13. Find the country that has all the vowels and no spaces in its name.

```mysql
SELECT name
  FROM world
 WHERE name     LIKE '%a%'
   AND name     LIKE '%e%'
   AND name     LIKE '%i%'
   AND name     LIKE '%o%'
   AND name     LIKE '%u%'
   AND name NOT LIKE '% %';
```

## 03. SELECT From Nobel

1. Change the query shown so that it displays Nobel prizes for 1950.

```mysql
SELECT yr, subject, winner
  FROM nobel
 WHERE yr = 1950;
```

2. Show who won the 1962 prize for Literature.

```mysql
SELECT winner
  FROM nobel
 WHERE subject = 'Literature'
   AND yr = 1962;
```

3. Show the year and subject that won 'Albert Einstein' his prize.

```mysql
SELECT yr, subject
  FROM nobel
 WHERE winner = 'Albert Einstein';
```

4. Give the name of the 'Peace' winners since the year 2000, including 2000.

```mysql
SELECT winner
  FROM nobel
 WHERE subject = 'Peace'
   AND yr >= 2000;
```

5. Show all details (yr, subject, winner) of the Literature prize winners for 1980 to 1989 inclusive.

```mysql
SELECT yr, subject, winner
  FROM nobel
 WHERE subject = 'Literature'
   AND yr BETWEEN 1980 AND 1989;
```

6. Show all details of the presidential winners:

   - Theodore Roosevelt

   - Woodrow Wilson

   - Jimmy Carter

   - Barack Obama

```mysql
SELECT *
  FROM nobel
 WHERE winner IN ('Theodore Roosevelt',
                   'Woodrow Wilson',
                   'Jimmy Carter',
                   'Barack Obama');
```

7. Show the winners with first name John.

```mysql
SELECT winner
  FROM nobel
 WHERE winner LIKE 'John%';
```

8. Show the Physics winners for 1980 together with the Chemistry winners for 1984.

```mysql
SELECT yr, subject, winner
  FROM nobel
 WHERE subject = 'Physics'   AND yr = 1980
    OR subject = 'Chemistry' AND yr = 1984;
```

9. Show the winners for 1980 excluding the Chemistry and Medicine.

```mysql
SELECT yr, subject, winner
  FROM nobel
 WHERE yr = 1980
   AND subject NOT IN ('Chemistry', 'Medicine');
```

10. Show who won a 'Medicine' prize in an early year (before 1910, not including 1910) together with winners of a 'Literature' prize in a later year (after 2004, including 2004).

```mysql
SELECT *
  FROM nobel
 WHERE subject = 'Medicine'   AND yr < 1910
    OR subject = 'Literature' AND yr >= 2004;
```

11. Find all details of the prize won by PETER GRÜNBERG.

```mysql
SELECT *
  FROM nobel
 WHERE winner = 'Peter Grünberg';
```

12. Find all details of the prize won by EUGENE O'NEILL.

```mysql
SELECT *
  FROM nobel
 WHERE winner = 'Eugene O\'NEILL';
```

13. List the winners, year and subject where the winner starts with Sir. Show the the most recent first, then by name order.

```mysql
  SELECT winner, yr, subject
    FROM nobel
   WHERE winner LIKE 'Sir%'
ORDER BY yr DESC, winner;
```

14. Show the 1984 winners and subject ordered by subject and winner name; but list Chemistry and Physics last.

```mysql
  SELECT winner, subject
    FROM nobel
   WHERE yr = 1984
ORDER BY subject IN ('Chemistry', 'Physics'), subject, winner;
```

## 04. SELECT in SELECT

1. List each country name where the population is larger than that of 'Russia'.

```mysql
SELECT name
  FROM world
 WHERE population > (SELECT population
                       FROM world
                      WHERE name = 'Russia');
```

2. Show the countries in Europe with a per capita GDP greater than 'United Kingdom'.

```mysql
SELECT name
  FROM world
 WHERE continent = 'Europe'
   AND gdp/population > (SELECT gdp/population
                           FROM world
                          WHERE name = 'United Kingdom');
```

3. List the name and continent of countries in the continents containing either Argentina or Australia. Order by name of the country.

```mysql
  SELECT name, continent
    FROM world
   WHERE continent IN (SELECT continent
                         FROM world
                        WHERE name IN ('Argentina', 'Australia'))
ORDER BY name;
```

4. Which country has a population that is more than Canada but less than Poland? Show the name and the population.

```mysql
SELECT name, population
  FROM world
 WHERE population > (SELECT population
                       FROM world
                      WHERE name = 'Canada')
   AND population < (SELECT population
                       FROM world
                      WHERE name = 'Poland');
```

5. Show the name and the population of each country in Europe. Show the population as a percentage of the population of Germany.

```mysql
SELECT name,
       CONCAT(ROUND(100*population / (SELECT population
                                     FROM world
                                    WHERE name = 'Germany')), '%')
  FROM world
 WHERE continent = 'Europe';
```

6. Which countries have a GDP greater than every country in Europe? Give the name only. (Some countries may have NULL gdp values)

```mysql
SELECT name
  FROM world
 WHERE gdp > ALL(SELECT gdp
                   FROM world
                  WHERE continent = 'Europe'
                    AND gdp > 0);
```

7. Find the largest country (by area) in each continent, show the continent, the name and the area.

```mysql
SELECT continent, name, area
  FROM world x
 WHERE area >= ALL(SELECT area
                     FROM world y
                    WHERE y.continent = x.continent
                      AND area > 0);
```

8. List each continent and the name of the country that comes first alphabetically.

```mysql
SELECT continent, name
  FROM world x
 WHERE name <= ALL(SELECT name
                    FROM world y
                   WHERE y.continent = x.continent);
```

9. Find the continents where all countries have a population <= 25000000. Then find the names of the countries associated with these continents. Show name, continent and population.

```mysql
SELECT name, continent, population
  FROM world x
 WHERE 25000000 >= ALL(SELECT population
                         FROM world y
                        WHERE y.continent = x.continent
                          AND y.population > 0);
```

10. Some countries have populations more than three times that of any of their neighbours (in the same continent). Give the countries and continents.

```mysql
SELECT name, continent
  FROM world x
 WHERE population > ALL(SELECT population * 3
                          FROM world y
                         WHERE y.continent = x.continent
                           AND y.name <> x.name);
```

