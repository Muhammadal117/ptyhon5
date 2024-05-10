import requests
from datetime import datetime

def obhavo(city_name):
    apikey = 'b3c3d89be78a3232cf87a44c48de2eb2'
    url = f'https://api.openweathermap.org/data/2.5/weather'

    parametr = {
        'q': city_name,
        'appid': apikey,
        'units': 'metric',
    }
    response = requests.get(url, params=parametr)
    data = response.json()

    try:
        lat = data['coord']['lat']
        lon = data['coord']['lon']
        havo = data['weather'][0]['main']
        desc = data['weather'][0]['description']
        harorat = data['main']['temp']
        feels_like = data['main']['feels_like']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        visibility = data['visibility']
        shamol_tez = data['wind']['speed']
        bulut = data['clouds']['all']
        sana = datetime.fromtimestamp(data['dt'])
        country = data['sys']['country']
        sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(data['sys']['sunset'])

        text = f'''
        Shahar nomi: {city_name}

        Havo: {havo}, {desc}
        Harorat: {harorat} ºC
        Tuyuladi: {feels_like} ºC
        Havo bosimi: {pressure}hPa
        Namlik: {humidity}%

        Ko'rish masofasi: {visibility}metr
        Shamol tezligi: {shamol_tez}m/s
        Bulutlar: {bulut}  ta

        Shahar kordinatalari:
        Uzunlik: {lat}° N
        Kenglik: {lon}° E

        Davlat: {country}
        Quyosh chiqishi: {sunrise}
        Quyosh botishi: {sunset}

        Malumot olingan vaqt: {sana}

        '''
        return text
    except:
        return 'Shahar topilmadi'
