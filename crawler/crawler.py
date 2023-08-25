import requests
from cassandra.cluster import Cluster
import uuid
from flask import Flask, jsonify
app = Flask(__name__)
API_KEY = 'a7922d978bb6fa5f83e4c6c5ffdd5fac'
CITY = 'Paris'
COUNTRY = 'FR'
cluster = Cluster(['172.17.0.2']) 
session = cluster.connect()
keyspace_query = """
	CREATE KEYSPACE IF NOT EXISTS mon_projet
	WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
"""
session.execute(keyspace_query)
session.set_keyspace('mon_projet')
table_query = """
        CREATE TABLE IF NOT EXISTS climat (
            id UUID PRIMARY KEY,
            temperature float,
            humidite float,
            pression float
        )
"""
session.execute(table_query)

def get_weather_data():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY}&appid={API_KEY}&mode=json&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Erreur lors de la requête API')
        return None
weather_data = get_weather_data()
#print(weather_data)
if weather_data:
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']
   # print(f"Température: {temperature} C")
   # print(f"Humidité: {humidity}%")
   # print(f"Pression: {pressure} hPa")
insert_query = """INSERT INTO climat (id, temperature, humidite, pression) VALUES (%s, %s, %s, %s)"""
data_to_insert = (uuid.uuid4(), int(temperature), int(humidity), int(pressure))
insert_data = session.execute(insert_query, data_to_insert)
@app.route('/weather', methods=['GET'])
def get_weather_data():

    select_query = f"SELECT * FROM climat"
    result = session.execute(select_query)


    if result:
        row = result[0]
        data = {
            'city': CITY,
            'country': COUNTRY,
            'temperature': row.temperature,
            'humidity': row.humidity,
            'pressure': row.pressure
        }
        return jsonify(data), 200
    else:
        return jsonify({'message': 'Le endpoint ne fonctionne pas'}), 404
if __name__ == '__main__':
    app.run()



