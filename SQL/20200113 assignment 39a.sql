CREATE TABLE fruit (
  id INTEGER,
  Name VARCHAR(255) NOT NULL,
  color varchar(255),
  taste varchar(255),
  PRIMARY KEY (id)   
);

CREATE TABLE stock (
  id INTEGER,
  fruit_id INTEGER ,
  description varchar(255) ,
  quantity INTEGER,
  price INTEGER,
  PRIMARY KEY (id), 
  FOREIGN KEY (fruit_id) REFERENCES fruit(id)
); 

INSERT INTO fruit(id,name,color,taste) VALUES(1,'lemon','yellow','sour');
INSERT INTO fruit(id,name, color, taste) VALUES(2,'orange', 'orange', 'juicy');
INSERT INTO fruit(id,name, color, taste) VALUES(3,'grapefruit', 'orange','bitter');
INSERT INTO fruit(id,name, color, taste) VALUES(4,'lime', 'green', 'sour');
INSERT INTO fruit(id,name, color, taste) VALUES(5,'tangerine', 'yellow', 'sweet');

update fruit set color  = 'yellow' where name ='orange';
Delete from fruit where name = 'tangerine';
select * from fruit;
select * from fruit where color = 'orange' or color = 'green';
delete from fruit;