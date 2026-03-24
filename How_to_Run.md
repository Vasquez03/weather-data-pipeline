# ▶️ How to Run

### 1. Clone the repository

``` bash
git clone https://github.com/Vasquez03/weather-data-pipeline.git
cd weather-data-pipeline
```

------------------------------------------------------------------------

### 2. Create virtual environment (recommended)

``` bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

------------------------------------------------------------------------

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

### 4. Configure database connection

Update the connection string in `db.py` with your SQL Server
credentials:

``` python
connection_string = "mssql+pyodbc://username:password@server/database?driver=ODBC+Driver+17+for+SQL+Server"
```

Make sure: - SQL Server is running - The database exists - You have the
correct ODBC driver installed

------------------------------------------------------------------------

### 5. Run the pipeline

``` bash
python main.py
```

------------------------------------------------------------------------

### 6. Expected output

-   Data is extracted from the weather API\
-   Transformed into structured format\
-   Loaded into SQL Server tables:
    -   `districts`
    -   `weather_data`

------------------------------------------------------------------------

## ⚠️ Notes

-   Avoid running multiple times without checking duplicates (handled in
    the pipeline)
-   Ensure internet connection for API calls

