import requests
import datetime

# Finds Lat and Long values from current location
location_url = 'http://ip-api.com/json'
location = requests.get(location_url)
location_data = eval(location.text)
lat = location_data['lat']
lon = location_data['lon']

# get a free API KEY from here https://openweathermap.org/price
API_KEY = ""

# Today's date and time
curr_date = datetime.datetime.now()

# Forecast Weather Data request
forecast_url = "http://api.openweathermap.org/data/2.5/forecast?lat={0}&lon={1}&units=metric&APPID={2}".format(lat, lon, API_KEY)
forecast = requests.get(forecast_url)
forecast_data = eval(forecast.text)['list']

# Current Weather Data request
weather_url = "http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&units=metric&APPID={2}".format(lat, lon, API_KEY)
weather = requests.get(weather_url)
weather_data = eval(weather.text)

# Day of week list
dayofweek_lst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print("\nLocation:", weather_data['name'] + ",", weather_data['sys']['country'])
print("\n************************ CURRENT WEATHER REPORT - Metric ************************")
print("\tTemp:", weather_data['main']['temp'], "\tWeather:", weather_data['weather'][0]['description'])
print("\n************************ 24h WEATHER FORECAST - Metric **************************")
for item in forecast_data:
    if int(item['dt_txt'][8:11]) == curr_date.day or (int(item['dt_txt'][8:11]) == curr_date.day+1 and int(item['dt_txt'][11:13]) < curr_date.hour):
        date = datetime.datetime.strptime(item['dt_txt'], "%Y-%m-%d %H:%M:%S")
        dayofweek = dayofweek_lst[date.weekday()]
        print("\t", dayofweek, item['dt_txt'][:-3], "\tTemp:", item['main']['temp'], "\tWeather:",item['weather'][0]['description'])
