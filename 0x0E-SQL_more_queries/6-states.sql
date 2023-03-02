-- Create db+table with unique id column that is prim key and can't be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT
		NOT NULL
		AUTO_INCREMENT
		UNIQUE KEY
		PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
