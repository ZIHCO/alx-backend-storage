-- SQL script that creates a table users

CREATE TABLE IF NOT EXISTS users (
		    id INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
		    email VARCHAR(255) UNIQUE,
		    name VARCHAR(255));
