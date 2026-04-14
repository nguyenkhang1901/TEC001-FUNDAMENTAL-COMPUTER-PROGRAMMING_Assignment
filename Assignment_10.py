import requests
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)


# Ex 1
def get_chuck_norris_joke():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    print(response.json()["value"])


# Ex 2
def get_weather():
    municipality = input("Enter the name of a municipality: ")
    api_key = "9ea6cb0ab6b9db383bc702eb0ebfdac2"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}"

    response = requests.get(url).json()
    description = response["weather"][0]["description"]
    temp_celsius = response["main"]["temp"] - 273.15

    print(f"Condition: {description}")
    print(f"Temperature: {temp_celsius:.1f} °C")


# Ex 3
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


@app.route("/prime_number/<int:number>")
def check_prime(number):
    return jsonify({"Number": number, "isPrime": is_prime(number)})


# Ex 4
@app.route("/airport/<icao>")
def airport_info(icao):
    conn = sqlite3.connect("airports.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT ident, name, municipality, iso_country FROM airport WHERE ident=?",
        (icao,),
    )
    result = cursor.fetchone()
    conn.close()

    if result:
        return jsonify(
            {
                "icao": result[0],
                "name": result[1],
                "city": result[2],
                "country": result[3],
            }
        )
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    get_chuck_norris_joke()
    get_weather()
    app.run(port=5000)
