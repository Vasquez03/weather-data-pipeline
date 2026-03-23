import requests


def extract_url(district, base_url):

    url = base_url+str(district['latitude'])+"&longitude="+str(district['longitude'])+"&daily=temperature_2m_max,temperature_2m_min,wind_speed_10m_max&timezone=auto"
   
    #extract the json from the URL and then convert it to json
    data = requests.get(url).json()

    return data