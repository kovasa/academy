USE workers;
CREATE TABLE IF NOT EXISTS subordinate (
id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
id_sup INT,
id_sub INT,
FOREIGN KEY(id_sup) REFERENCES person(id),
FOREIGN KEY(id_sub) REFERENCES person(id)
);

INSERT INTO person ( id, first_name, last_name, salary, post_id) VALUES ( null, 'Kiril', 'Kirilov', 15000, 1);
INSERT INTO person ( id, first_name, last_name, salary, post_id) VALUES ( null, 'Vicor', 'Victorov', 60000, 2);
INSERT INTO person ( id, first_name, last_name, salary, post_id) VALUES ( null, 'Sergey', 'Sergeev', 80000, 2);

INSERT INTO subordinate (id, id_sup, id_sub) VALUES (null, 2, 1);
INSERT INTO subordinate (id, id_sup, id_sub) VALUES (null, 2, 5);
INSERT INTO subordinate (id, id_sup, id_sub) VALUES (null, 4, 3);
INSERT INTO subordinate (id, id_sup, id_sub) VALUES (null, 6, 4);
INSERT INTO subordinate (id, id_sup, id_sub) VALUES (null, 7, 6);

SELECT per1.last_name, per2.last_name
FROM subordinate sub
INNER JOIN person per1 ON per1.id=sub.id_sup
INNER JOIN person per2 ON per2.id=sub.id_sub
WHERE per1.last_name = 'Petrov'

