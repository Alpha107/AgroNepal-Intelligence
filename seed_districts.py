import os
import urllib.request
import json

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(DATA_DIR, exist_ok=True)
FILE_PATH = os.path.join(DATA_DIR, 'nepal_districts.geojson')

url = "https://raw.githubusercontent.com/mesaugat/geoJSON-Nepal/master/nepal-districts.geojson"

print(f"Downloading GeoJSON from {url}...")
try:
    with urllib.request.urlopen(url) as response:
        if response.status == 200:
            data = json.loads(response.read().decode())
            with open(FILE_PATH, 'w', encoding='utf-8') as f:
                json.dump(data, f)
            print("Successfully downloaded and saved GeoJSON.")
        else:
            print(f"Failed to download: {response.status}")
except Exception as e:
    print(f"Error occurred: {e}")
