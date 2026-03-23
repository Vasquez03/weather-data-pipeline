ALTER TABLE weather_data
ADD CONSTRAINT UQ_weather_data_district_time UNIQUE (ID_Districts, time);