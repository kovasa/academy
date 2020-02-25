CREATE DATABASE IF NOT EXISTS workers;
USE workers;
CREATE TABLE IF NOT EXISTS person (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
    first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
    salary int NOT NULL
);
INSERT INTO person ( id, first_name, last_name, salary) VALUES ( null, 'Ivan', 'Ivanov', 10000);
INSERT INTO person ( id, first_name, last_name, salary) VALUES ( null, 'Petr', 'Petrov', 20000);
INSERT INTO person ( id, first_name, last_name, salary) VALUES ( null, 'Bob', 'Bobov', 30000);
INSERT INTO person ( id, first_name, last_name, salary) VALUES ( null, 'Karl', 'Karlov', 40000);
CREATE TABLE IF NOT EXISTS post (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
    post_name VARCHAR(30) NOT NULL
);
INSERT INTO post ( id, post_name) VALUES ( null, 'manager');
INSERT INTO post ( id, post_name) VALUES ( null, 'developer');
ALTER TABLE person ADD post_id INTEGER NOT NULL;
UPDATE person SET post_id=1 WHERE id IN (1,2);
UPDATE person SET post_id=2 WHERE id IN (3,4);
SELECT per.first_name, per.last_name, pst.post_name, per.salary
FROM person per
INNER JOIN post pst ON per.post_id=pst.id;



