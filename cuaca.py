import requests

kota = input("Masukan nama kota: ")

geo = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={kota}&count=1")
data_geo = geo.json()

if not data_geo.get("results"):
    print("Kota tidak ditemukan!")
else:
    lat = data_geo["results"][0]["latitude"]
    lon = data_geo["results"][0]["longitude"]
    nama_kota = data_geo["results"][0]["name"]

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    cuaca = requests.get(url)
    data_cuaca = cuaca.json()["current_weather"]

    print(f"\n=== CUACA DI {nama_kota.upper()} ===")
    print(f"Suhu  : {data_cuaca['temperature']} C")
    print(f"Angin : {data_cuaca['windspeed']} km/h")
