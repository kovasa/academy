USE workers;
SELECT per.first_name, per.last_name, pst.post_name, per.salary 
FROM person per
INNER JOIN post pst ON per.post_id=pst.id
WHERE per.salary<30000;

SELECT per.first_name, per.last_name, pst.post_name, per.salary 
FROM person per
INNER JOIN post pst ON per.post_id=pst.id
WHERE pst.post_name = 'developer' and per.salary < 40000;