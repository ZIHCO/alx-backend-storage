-- SQL script that creates a table users

CREATE TABLE IF NOT EXISTS users (
		    id INT AUTO_INCREMENT UNIQUE PRIMARY_KEY,
		    email VARCHAR(255) UNIQUE,
		    name VARCHAR(255));
