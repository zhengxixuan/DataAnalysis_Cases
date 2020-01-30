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

## 05. SUM and COUNT

1. Show the total population of the world.

```mysql
SELECT SUM(population)
  FROM world;
```

2. List all the continents - just once each.

```mysql
SELECT DISTINCT continent
           FROM world;
```

3. Give the total GDP of Africa.

```mysql
SELECT SUM(gdp)
  FROM world
 WHERE continent = 'Africa';
```

4. How many countries have an area of at least 1000000.

```mysql
SELECT COUNT(name)
  FROM world
 WHERE area > 1000000;
```

5. What is the total population of ('Estonia', 'Latvia', 'Lithuania').

```mysql
SELECT SUM(population)
  FROM world
 WHERE name IN ('Estonia', 'Latvia', 'Lithuania');
```

6. For each continent show the continent and number of countries.

```mysql
  SELECT continent, COUNT(name)
    FROM world
GROUP BY continent;
```

7. For each continent show the continent and number of countries with populations of at least 10 million.

```mysql
  SELECT continent, COUNT(name)
    FROM world
   WHERE population > 10000000
GROUP BY continent;
```

8. List the continents that have a total population of at least 100 million.

```mysql
  SELECT continent
    FROM world
GROUP BY continent
  HAVING SUM(population) > 100000000;
```

## 06. JOIN

1. Modify the example to show the matchid and player name for all goals scored by Germany. To identify German players, check for: teamid = 'GER'

```mysql
SELECT matchid, player
  FROM goal
 WHERE teamid = 'GER';
```

2. Show id, stadium, team1, team2 for just game 1012.

```mysql
SELECT id, stadium, team1, team2
  FROM game
 WHERE id = 1012;
```

3. Modify the code to show the player, teamid, stadium and mdate and for every German goal.

```mysql
SELECT player, teamid, stadium, mdate
  FROM game JOIN goal ON id = matchid
 WHERE teamid = 'GER';
```

4. Show the team1, team2 and player for every goal scored by a player called Mario player LIKE 'Mario%'

```mysql
SELECT team1, team2, player
  FROM game JOIN goal ON id = matchid
 WHERE player LIKE 'Mario%';
```

5. Show player, teamid, coach, gtime for all goals scored in the first 10 minutes gtime<=10

```mysql
SELECT player, teamid, coach, gtime
  FROM goal JOIN eteam ON teamid = id
 WHERE gtime <= 10;
```

6. List the the dates of the matches and the name of the team in which 'Fernando Santos' was the team1 coach.

```mysql
SELECT mdate, teamname
  FROM game JOIN eteam ON team1 = eteam.id
 WHERE coach = 'Fernando Santos';
```

7. List the player for every goal scored in a game where the stadium was 'National Stadium, Warsaw'.

```mysql
SELECT player
  FROM goal JOIN game ON matchid = id
 WHERE stadium = 'National Stadium, Warsaw';
```

8. The example query shows all goals scored in the Germany-Greece quarterfinal. Instead show the name of all players who scored a goal against Germany.

```mysql
SELECT DISTINCT player
  FROM goal JOIN game ON matchid = id
 WHERE (team1 = 'GER' OR team2 = 'GER')
   AND teamid != 'GER';
```

9. Show teamname and the total number of goals scored.

```mysql
  SELECT teamname, COUNT(teamid)
    FROM eteam JOIN goal ON eteam.id = teamid
GROUP BY teamname;
```

10. Show the stadium and the number of goals scored in each stadium.

```mysql
  SELECT stadium, COUNT(stadium)
    FROM game JOIN goal ON id = matchid
GROUP BY stadium;
```

11. For every match involving 'POL', show the matchid, date and the number of goals scored.

```mysql
  SELECT matchid, mdate, COUNT(*)
    FROM game JOIN goal ON id = matchid
   WHERE (team1 = 'POL' OR team2 = 'POL')
GROUP BY matchid, mdate;
```

12. For every match where 'GER' scored, show matchid, match date and the number of goals scored by 'GER'.

```MYSQL
  SELECT matchid, mdate, COUNT(*)
    FROM game JOIN goal ON id = matchid
   WHERE (team1 = 'GER' OR team2 = 'GER')
     AND teamid = 'GER'
GROUP BY matchid, mdate;
```

13. List every match with the goals scored by each team as shown. Sort your result by mdate, matchid, team1 and team2.

```mysql
   SELECT mdate,
          team1,
          SUM(CASE WHEN teamid = team1 THEN 1 ELSE 0 END) score1,
          team2,
          SUM(CASE WHEN teamid = team2 THEN 1 ELSE 0 END) score2

     FROM game
LEFT JOIN goal ON id = matchid

 GROUP BY mdate, team1, team2
 ORDER BY mdate, team1, team2;
```

## 07. More JOIN Operations

1. List the films where the yr is 1962. Show id, title.

```mysql
SELECT id, title
  FROM movie
 WHERE yr = 1962;
```

2. Give year of 'Citizen Kane'.

```mysql
SELECT yr
  FROM movie
 WHERE title = 'Citizen Kane';
```

3. List all of the Star Trek movies, include the id, title and yr (all of these movies include the words Star Trek in the title). Order results by year.

```mysql
  SELECT id, title, yr
    FROM movie
   WHERE title LIKE 'Star Trek%'
ORDER BY yr;
```

4. What id number does the actor 'Glenn Close' have?

```mysql
SELECT id
  FROM actor
 WHERE name = 'Glenn Close';
```

5. What is the id of the film 'Casablanca'?

```mysql
SELECT id
  FROM movie
 WHERE title = 'Casablanca';
```

6. Obtain the cast list for 'Casablanca'.

```mysql
SELECT name
  FROM movie
  JOIN casting ON movie.id = casting.movieid
  JOIN actor   ON actor.id = casting.actorid
 WHERE title= 'Casablanca';
```

7. Obtain the cast list for the film 'Alien'.

```mysql
SELECT name
  FROM movie
  JOIN casting ON movie.id = casting.movieid
  JOIN actor   ON actor.id = casting.actorid
 WHERE title = 'Alien';
```

8. List the films in which 'Harrison Ford' has appeared.

```mysql
SELECT title
  FROM movie
  JOIN casting ON movie.id = casting.movieid
  JOIN actor   ON actor.id = casting.actorid
 WHERE actor.name = 'Harrison Ford';
```

9. List the films where 'Harrison Ford' has appeared - but not in the starring role. Note: the 'ord' field of casting gives the position of the actor. If 'ord=1' then this actor is in the starring role.

```mysql
SELECT title
  FROM movie
  JOIN casting ON movie.id = casting.movieid
  JOIN actor   ON actor.id = casting.actorid
 WHERE actor.name = 'Harrison Ford'
   AND ord != 1;
```

10. List the films together with the leading star for all 1962 films.

```mysql
SELECT title, name
  FROM movie
  JOIN casting ON movie.id = casting.movieid
  JOIN actor   ON actor.id = casting.actorid
 WHERE yr = 1962
   AND ord = 1;
```

11. Which were the busiest years for 'Rock Hudson', show the year and the number of movies he made each year for any year in which he made more than 2 movies.

```mysql
  SELECT yr, COUNT(title)
    FROM movie
    JOIN casting ON movie.id = movieid
    JOIN actor   ON actorid = actor.id
   WHERE name = 'Rock Hudson'
GROUP BY yr
  HAVING COUNT(title) > 1;
```

12. List the film title and the leading actor for all of the films 'Julie Andrews' played in.

```mysql
SELECT title, name
  FROM casting
  JOIN movie ON casting.movieid = movie.id AND ord = 1
  JOIN actor ON casting.actorid = actor.id
 WHERE movie.id IN
       (SELECT movieid
          FROM casting
         WHERE actorid IN
         (SELECT id FROM actor
           WHERE name = 'Julie Andrews'));
```

13. Obtain a list, in alphabetical order, of actors who've had at least 15 **starring** roles.

```mysql
  SELECT name
    FROM actor
    JOIN casting ON casting.actorid = actor.id
    JOIN movie   ON casting.movieid = movie.id
   WHERE actorid IN
         (SELECT actorid
            FROM casting
           WHERE ord = 1
        GROUP BY actorid
          HAVING COUNT(actorid) >= 15)
GROUP BY name;
```

14. List the films released in the year 1978 ordered by the number of actors in the cast, then by title.

```mysql
  SELECT title, COUNT(actorid)
    FROM movie
    JOIN casting ON casting.movieid = movie.id
    JOIN actor   ON casting.actorid = actor.id
   WHERE yr = 1978
GROUP BY title
ORDER BY COUNT(actorid) DESC, title;
```

15. List all the people who have worked with 'Art Garfunkel'.

```mysql
SELECT DISTINCT name
  FROM actor
  JOIN casting ON casting.actorid = actor.id
  JOIN movie   ON casting.movieid = movie.id
 WHERE name != 'Art Garfunkel'
   AND movieid IN
       (SELECT movieid
          FROM casting
          JOIN actor ON casting.actorid = actor.id
          JOIN movie ON casting.movieid = movie.id
         WHERE name = 'Art Garfunkel');
```

## 08. Using NULL

1. List the teachers who have NULL for their department.

```mysql
SELECT name
  FROM teacher
 WHERE dept IS NULL;
```

2. Note the INNER JOIN misses the teachers with no department and the departments with no teacher.

```mysql
    SELECT teacher.name, dept.name
      FROM teacher
INNER JOIN dept ON teacher.dept = dept.id;
```

3. Use a different JOIN so that all teachers are listed.

```mysql
   SELECT teacher.name, dept.name
     FROM teacher
LEFT JOIN dept ON teacher.dept = dept.id;
```

4. Use a different JOIN so that all departments are listed.

```mysql
    SELECT teacher.name, dept.name
      FROM teacher
RIGHT JOIN dept on teacher.dept = dept.id;
```

5. Use COALESCE to print the mobile number. Use the number '07986 444 2266' if there is no number given. Show teacher name and mobile number or '07986 444 2266'.

```mysql
SELECT name, COALESCE(mobile, '07986 444 2266')
  FROM teacher;
```

6. Use the COALESCE function and a LEFT JOIN to print the teacher name and department name. Use the string 'None' where there is no department.

```mysql
   SELECT teacher.name, COALESCE(dept.name, 'None') AS deptartment
     FROM teacher
LEFT JOIN dept ON teacher.dept = dept.id;
```

7. Use COUNT to show the number of teachers and the number of mobile phones.

```mysql
SELECT COUNT(name)   AS teachers,
       COUNT(mobile) AS mobiles
  FROM teacher;
```

8. Use COUNT and GROUP BY dept.name to show each department and the number of staff. Use a RIGHT JOIN to ensure that the Engineering department is listed.

```mysql
    SELECT dept.name, COUNT(teacher.dept) AS staff
      FROM teacher
RIGHT JOIN dept ON teacher.dept = dept.id
  GROUP BY dept.name;
```

9. Use CASE to show the name of each teacher followed by 'Sci' if the teacher is in dept 1 or 2 and 'Art' otherwise.

```mysql
SELECT name,
       CASE WHEN dept = 1 OR dept = 2
            THEN 'Sci'
            ELSE 'Art'
        END AS dept
  FROM teacher;
```

10. Use CASE to show the name of each teacher followed by 'Sci' if the teacher is in dept 1 or 2, show 'Art' if the teacher's dept is 3 and 'None' otherwise.

```mysql
SELECT name,
       CASE WHEN dept = 1 OR dept = 2
            THEN 'Sci'
            WHEN dept = 3
            THEN 'Art'
            ELSE 'None'
        END AS dept
  FROM teacher;
```

## 09. Self JOIN

1. How many stops are in the database.

```mysql
SELECT COUNT(DISTINCT stop)
  FROM route
  JOIN stops ON route.stop = stops.id;
```

2. Find the id value for the stop 'Craiglockhart'.

```mysql
SELECT id
  FROM stops
 WHERE name = 'Craiglockhart';
```

3. Give the id and the name for the stops on the '4' 'LRT' service.

```mysql
SELECT id, name
  FROM stops
  JOIN route ON stops.id = route.stop
 WHERE num = '4'
   AND company = 'LRT';
```

4. The query shown gives the number of routes that visit either London Road (149) or Craiglockhart (53). Run the query and notice the two services that link these stops have a count of 2. Add a HAVING clause to restrict the output to these two routes.

```mysql
  SELECT company, num, COUNT(*)
    FROM route
   WHERE stop = 149 OR stop = 53
GROUP BY company, num
  HAVING COUNT(*) = 2;
```

5. Execute the self join shown and observe that b.stop gives all the places you can get to from Craiglockhart, without changing routes. Change the query so that it shows the services from Craiglockhart to London Road.

```mysql
SELECT a.company, a.num, a.stop, b.stop
  FROM route a
  JOIN route b ON a.company = b.company AND a.num = b.num
 WHERE a.stop = 53
   AND b.stop = 149;
```