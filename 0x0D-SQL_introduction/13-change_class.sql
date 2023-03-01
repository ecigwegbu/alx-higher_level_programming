-- Score too low

DELETE IF EXISTS second_table
	WHERE score <= 5;
