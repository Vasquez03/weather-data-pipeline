## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Vasquez03/weather-data-pipeline.git
cd weather-data-pipeline

### 2. Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

### 3. Install dependencies
```bash
pip install -r requirements.txt

### 4. Configure database connection
```bash
connection_string = "mssql+pyodbc://username:password@server/database?driver=ODBC+Driver+17+for+SQL+Server"




Configure database connection
```bash

- SQL Server is running
- The database exists
- You have the correct ODBC driver installed


5. Run the pipeline
```bash

python main.py


6. Expected output
Data is extracted from the weather API
Transformed into structured format
Loaded into SQL Server tables:
districts
weather_data