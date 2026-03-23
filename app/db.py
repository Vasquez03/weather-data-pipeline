from sqlalchemy import text, create_engine

def connect_SQL():
    engine = create_engine(
    "mssql+pyodbc://@localhost/weather_pipeline?driver=ODBC+Driver+18+for+SQL+Server&trusted_connection=yes&TrustServerCertificate=yes")

    return engine



def table_has_data(engine, table_name):
    query = text(f"SELECT COUNT(*) FROM {table_name}")

    with engine.connect() as conn:
        result = conn.execute(query)
        count = result.scalar()

    return count > 0




