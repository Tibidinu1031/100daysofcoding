import requests, json

timezone = "GMT"
latitude = 37.47
longitude = 122.25


result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude="
                      f"{latitude}&longitude="
                      f"{longitude}&daily=weather_code,temperature_2m_max,t"
                      f"emperature_2m_min&timezone={timezone.upper()}")
user = result.json()


tmin = user['daily']['temperature_2m_min'][0]
tmax = user['daily']['temperature_2m_max'][0]

print()
print()
print(f"Temperature min is: {tmin}*C,\nTemperature max is: {tmax}*C")