def send_district_SQL (district_df,engine):
    
    district_df.to_sql("districts", engine, if_exists="append", index=False)

def send_weather_data_SQL (final_df,engine):

    final_df.to_sql("weather_data", engine, if_exists="append", index=False)