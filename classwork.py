import requests

s_city = "Moscow,RU"
appid = "629eefae1cacb983cd7f14147b9c969e"

res = requests.get("https://api.openweathermap.org/data/2.5/weather",
params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()


print('Город:',s_city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:",data['main']['temp_min'])
print("Максимальная температура:",data['main']['temp_max'])

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",
    '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",
    i['weather'][0]['description'], ">")
print("____________________________")