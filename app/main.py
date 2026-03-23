from extract import extract_url
from transform import transform_json, join_table, convert_district_df
from db import connect_SQL, table_has_data
from load import send_district_SQL, send_weather_data_SQL



districts = [
    {'ID_Districts':1,'city':'Palmares', 'latitude': 10.054149, 'longitude': -84.437782},
    {'ID_Districts':2, 'city':'Grecia', 'latitude': 10.074208, 'longitude': -84.313382},
    {'ID_Districts':3, 'city':'San Ramón', 'latitude': 10.088456, 'longitude': -84.469603},
    {'ID_Districts':4, 'city':'Atenas', 'latitude': 9.976157, 'longitude':  -84.379430},
    {'ID_Districts':5, 'city':'Zarcero', 'latitude': 10.185946, 'longitude':  -84.393393}
    
]

#automate the searching for the differents locations using the previous dictionary
base_url = "https://api.open-meteo.com/v1/forecast?latitude="


def main():
    print("Starting the pipiline.....")

    engine = connect_SQL()
    print("Connected to SQL server.........")

    dfs = []
    
    for district in districts:
        print(f"Extracting and transforming data for {district['city']} ")
        data = extract_url(district, base_url)
        df = transform_json(data, district)
        dfs.append(df)

    print("Joining the table ") 
    final_df = join_table(dfs)
    district_df = convert_district_df(districts)
    print(f"Weather dataset ready. Rows: {len(final_df)}.......... ")

    if not table_has_data(engine, "districts"):
        print("Loading districts table...")
        send_district_SQL(district_df, engine)
    else:
        print("Districts table already has data. Skipping load.")

    send_weather_data_SQL(final_df, engine)
    print("Weather data loaded successfully.")
    print("Pipeline executed correctly.")

if __name__ == "__main__":
    main()


