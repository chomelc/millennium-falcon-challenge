CREATE TABLE ROUTES (
	origin TEXT NOT NULL,
   destination TEXT NOT NULL,
	travel_time INTEGER NOT NULL CHECK (travel_time >= 0)
);

INSERT INTO ROUTES (origin, destination, travel_time)
VALUES 
   ("Tatooine", "Dagobah", 6),
   ("Dagobah", "Endor", 4),
   ("Dagobah", "Hoth" , 1),
   ("Hoth", "Endor" , 1),
   ("Tatooine", "Hoth", 6);