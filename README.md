# 🌦️ Weather Data Pipeline

## 📌 Overview

This project implements an end-to-end data pipeline that extracts,
transforms, and loads (ETL) daily weather data using Python and SQL
Server.

The pipeline retrieves data from a public weather API for selected
districts in Alajuela, Costa Rica, processes it, and stores it in a
relational database for further analysis and visualization.

\---

## 🎯 Objectives

* Build a modular ETL pipeline using Python\\
* Integrate external API data into a structured database\\
* Design a relational schema for weather data\\
* Ensure data quality through validation and duplicate handling

\---

## 🛠️ Technologies Used

* Python
* pandas
* requests
* SQL Server
* SQLAlchemy
* pyodbc

\---

## ⚙️ Pipeline Architecture

API → Extract → Transform → Load → SQL Server

\---

## 📂 Project Structure

&#x20;   .
    ├── extract.py     # Extracts weather data from API
    ├── transform.py   # Transforms JSON into structured DataFrames
    ├── load.py        # Loads data into SQL Server
    ├── db.py          # Manages database connection and validation
    └── main.py        # Orchestrates the ETL pipeline


\---

## 🗄️ Data Model

### districts

Column         Description

\---

ID\_Districts   Primary key
city           District name
latitude       Geographic coordinate
longitude      Geographic coordinate

### weather\_data

Column            Description

\---

time              Timestamp of observation
temperature\_max   Maximum temperature
temperature\_min   Minimum temperature
wind\_speed\_max    Maximum wind speed
ID\_Districts      Foreign key

\---

## 🚀 Key Features

* Automated data extraction from a public API\\
* JSON processing and transformation using pandas\\
* Structured storage in SQL Server\\
* Duplicate prevention using pandas and SQL constraints\\
* Validation logic to prevent reloading static district data

\---

## 🔮 Future Improvements

* Integration with Power BI for visualization\\
* Pipeline scheduling (cron or Airflow)\\
* Enhanced logging and monitoring\\
* Error handling and retry mechanisms

\---

## 👨‍💻 Author

Edwin Vásquez Vargas
Electrical Engineer

