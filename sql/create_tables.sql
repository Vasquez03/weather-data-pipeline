CREATE TABLE districts(
	ID_Districts INT PRIMARY KEY NOT NULL,
	city VARCHAR(50),
	latitude FLOAT,
	longitude FLOAT
);


CREATE TABLE weather_data(
	ID_Weather INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
	time DATE NOT NULL,
	temperature_max FLOAT,
	temperature_min FLOAT,
	wind_speed_max FLOAT,
	ID_Districts INT NOT NULL,
	FOREIGN KEY (ID_Districts) REFERENCES districts(ID_Districts)
);