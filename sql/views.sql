CREATE VIEW weather_view AS
SELECT
	d.city,
	w.time,
	w.temperature_max,
	w.temperature_min,
	w.wind_speed_max

FROM districts d
INNER JOIN weather_data w
	ON w.ID_Districts = d.ID_Districts


SELECT * FROM weather_view 

