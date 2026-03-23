# Weather Data Pipeline

## Project Overview
This project builds an end-to-end weather data pipeline using Python, SQL Server, and a public weather API.

The objective is to collect daily weather data from selected districts in Alajuela, transform it, and store it in a relational database for further analysis.

## Technologies Used
- Python
- pandas
- requests
- SQL Server
- SQLAlchemy

## Pipeline Architecture
API -> Python -> SQL Server --> Power BI

## Project Structure
- extract.py: extracts weather data from the API
- transform.py: transforms JSON data into pandas DataFrames
- db.py: handles SQL Server connection and validation
- load.py: loads data into SQL Server
- main.py: orchestrates the pipeline execution

## Data Model
### districts
Stores district information:
- ID_Districts
- city
- latitude
- longitude

### weather_data
Stores daily weather observations:
- time
- temperature_max
- temperature_min
- wind_speed_max
- ID_Districts

## Key Features
- API data extraction
- JSON transformation with pandas
- Relational schema in SQL Server
- Duplicate prevention using pandas and SQL unique constraint
- Validation to avoid reloading district catalog

## Future Improvements
- Add scheduling
- Add more robust logging