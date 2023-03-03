--  subquery cities of california

SELECT id, name FROM cities
	WHERE id='states.name'California
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT
		NOT NULL
		AUTO_INCREMENT
		UNIQUE KEY
		PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
