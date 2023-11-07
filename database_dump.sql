PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE user (
	id INTEGER NOT NULL, 
	username VARCHAR(64) NOT NULL, 
	first_name VARCHAR(15) NOT NULL, 
	last_name VARCHAR(15) NOT NULL, 
	email_address VARCHAR(120) NOT NULL, 
	category VARCHAR(30) NOT NULL, 
	password_hash VARCHAR(120) NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO user VALUES(1,'florenjeri','Florence','Kamau','kamaufnjeri2018@gmail.com','artist','$2b$12$8ACuzm8.m8RVRier40tXA.m9j1pmQMzcZbDya6lipCXngmu/QRxaW');
INSERT INTO user VALUES(2,'bettykamau','betty','Kamau','bettykamau@gmail.com','artist','$2b$12$VmLo4S/Q5sSluTEDZ/7DZ.IutD0clb/KJcrygrzqBmKHSWDg7vTjC');
INSERT INTO user VALUES(3,'virgkamau','virg','Kamau','virgkamau@gmail.com','artist','$2b$12$QEbPn0oxqtG/CNpu2hXy2uZeXoEWpnSdVjUDtQnunsTiTZjISnZNy');
INSERT INTO user VALUES(4,'flozzykamau','Flozzy','Kamau','flozzykamau@gmail.com','artist','$2b$12$HAmqYDTDBZxeMEiezJKyIeFu22GKzPgXj0fjZoRBYh39GBcsc7rj6');
INSERT INTO user VALUES(5,'bettygitonga','betty','gitonga','bettygitonga@gmail.com','artist','$2b$12$XXkba9l5dr513Pq0CEXVy.tMeo9t72gMFOevzaY1j1ixp6D7Tqcre');
INSERT INTO user VALUES(6,'rosewambura','rose','wambura','rose@gmail.com','artist','$2b$12$y9hSe0ON/ryuBwxAvEjlfeG21Dgby8zAM1CR8EWO7FnLkLfwD1ocW');
INSERT INTO user VALUES(7,'eladiogomez','eladio','gomez','eladiogomez@gmail.com','art_enthusiast','$2b$12$LoEygcY7Le78R3QkCtcZy.ru2q7oZQWUN4HlgM/vEY.4zf1DoHmzq');
INSERT INTO user VALUES(8,'oliviamonte','olivia','montenegro','oliviamonte@gmail.com','art_enthusiast','$2b$12$/EeJ8ohlkuAakgPdIJk2c.Qp4OKWZT5tLadBxhWte4ujbdMN.ArAG');
CREATE TABLE artwork (
	id INTEGER NOT NULL, 
	title VARCHAR(255) NOT NULL, 
	description VARCHAR(1024) NOT NULL, 
	price VARCHAR NOT NULL, 
	category VARCHAR NOT NULL, 
	artwork_url VARCHAR NOT NULL, 
	owner_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owner_id) REFERENCES user (id)
);
INSERT INTO artwork VALUES(5,'Painting 1','A painting by betty for viewing','250.0','painting','https://res.cloudinary.com/dpbkthtxd/image/upload/v1698145758/my_pics/995d4bd3-a7dc-403f-810f-6f5897e022bb.jpg',2);
INSERT INTO artwork VALUES(6,'Painting 2','A painting for viewing and enjoying. ','270.0','painting','https://res.cloudinary.com/dpbkthtxd/image/upload/v1698145807/my_pics/2ce61cab-e0d3-4cf8-8a2b-52ac3dcf69bc.jpg',2);
INSERT INTO artwork VALUES(7,'Sculpture 1','A sculpture i made for viewing and decoration','450.0','sculpture','https://res.cloudinary.com/dpbkthtxd/image/upload/v1698145994/my_pics/43fcd843-3cf8-4d6c-a595-48e8c69732a1.jpg',3);
INSERT INTO artwork VALUES(8,'Sculpture 2','A sculpture for viewing and can also be bought','550.0','sculpture','https://res.cloudinary.com/dpbkthtxd/image/upload/v1698146048/my_pics/33c176ca-b340-4041-8b93-ecce3a3481c0.jpg',3);
INSERT INTO artwork VALUES(9,'Sculpture 3','An artwork for viewing and decoration','770.0','sculpture','https://res.cloudinary.com/dpbkthtxd/image/upload/v1698146110/my_pics/404b5307-b18b-40ef-a3ff-fc88300e6438.jpg',3);
INSERT INTO artwork VALUES(10,'My sculpture','A sculpture by me for viewing','630.0','sculpture','https://res.cloudinary.com/dpbkthtxd/image/upload/v1698146340/my_pics/786215ec-5466-4bb5-962f-d00294522f9d.jpg',4);
INSERT INTO artwork VALUES(11,'My sculpture 2','A sculpture for viewing and enjoying','450.0','sculpture','https://res.cloudinary.com/dpbkthtxd/image/upload/v1698146411/my_pics/71872a87-a734-4980-83ac-a8bc13a5c237.jpg',4);
INSERT INTO artwork VALUES(12,'Photo 1','Photo 1 i took when in London','234.0','photography','https://res.cloudinary.com/dpbkthtxd/image/upload/v1698146573/my_pics/5c47b883-8844-49a7-87ac-79ff7bd321d8.jpg',5);
INSERT INTO artwork VALUES(13,'Photography 2','An image i took for viewing and enjoying. it is one of my best photos','300.0','photography','https://res.cloudinary.com/dpbkthtxd/image/upload/v1698146820/my_pics/bd78d546-0d52-405d-af8c-00eeb2a70c38.jpg',5);
INSERT INTO artwork VALUES(14,'Photography 3','An artwork I love so much. I have a sentimental attachment to it','700.0','photography','https://res.cloudinary.com/dpbkthtxd/image/upload/v1698146883/my_pics/bfe961f7-448b-4b17-972e-07b7c60116ca.jpg',5);
INSERT INTO artwork VALUES(15,'My photo one','A photo I love dearly and I would like you to also view it','770.0','photography','https://res.cloudinary.com/dpbkthtxd/image/upload/v1698147000/my_pics/a96654a5-777a-49a1-a5ef-07bcc03a7345.jpg',6);
INSERT INTO artwork VALUES(16,'My photo two','A photo I took during a very rough time. It motivates me to keep trying','650.0','photography','https://res.cloudinary.com/dpbkthtxd/image/upload/v1698147084/my_pics/7fafcd25-182f-43ef-928d-2d8694e10623.jpg',6);
INSERT INTO artwork VALUES(17,'Artwork 5','An artwork for viewing and pleasure','500.0','painting','https://res.cloudinary.com/dpbkthtxd/image/upload/v1698242058/my_pics/a85b8363-01d0-48db-9786-76279a7dbdc3.jpg',1);
INSERT INTO artwork VALUES(19,'My trial','azsnjannsjas','220.0','painting','https://res.cloudinary.com/dpbkthtxd/image/upload/v1698318587/my_pics/23e44507-7f42-441a-9363-2fe3c09b55c0.jpg',NULL);
CREATE UNIQUE INDEX ix_user_username ON user (username);
CREATE INDEX ix_user_last_name ON user (last_name);
CREATE UNIQUE INDEX ix_user_email_address ON user (email_address);
CREATE INDEX ix_user_first_name ON user (first_name);
CREATE INDEX ix_artwork_category ON artwork (category);
CREATE UNIQUE INDEX ix_artwork_artwork_url ON artwork (artwork_url);
CREATE UNIQUE INDEX ix_artwork_title ON artwork (title);
CREATE INDEX ix_artwork_description ON artwork (description);
CREATE INDEX ix_artwork_price ON artwork (price);
COMMIT;
