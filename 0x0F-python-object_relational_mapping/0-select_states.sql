-- Create states table in hbtn_0e_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
);
INSERT INTO states (name) VALUES ("Carlifornia"), ("Arizona"), ("Texas"),
("New York"), ("Nevada");
