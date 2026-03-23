import pandas as pd

def transform_json(data, district):
    dfs = []
    df = pd.DataFrame({
        "time": data["daily"]["time"],
        "temperature_max": data["daily"]["temperature_2m_max"],
        "temperature_min": data["daily"]["temperature_2m_min"],
        "wind_speed_max":  data["daily"]["wind_speed_10m_max"]
        })

    df["ID_Districts"] = district["ID_Districts"]

    return df


def join_table(dfs):
    final_df = pd.concat(dfs, ignore_index=True)
    fina_df = final_df.drop_duplicates(subset=["time","ID_Districts"])

    return final_df


def convert_district_df(districts):
    district_df = pd.DataFrame(districts)

    return district_df