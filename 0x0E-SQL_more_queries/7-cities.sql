-- Create Cities table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF EXISTS hbtn_0d_usa IF NOT EXISTS hbtn_0d_usa.cities (
	id INT
		NOT NULL
		AUTO_INCREMENT
		UNIQUE KEY
		PRIMARY KEY,
	state_id INT
		NOT NULL,
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
	name VARCHAR(256)
		NOT NULL
);
