import pgeocode
nomi = pgeocode.Nominatim('IN')
#print(nomi.query_postal_code("226021").latitude)
#print(nomi.query_postal_code("226021").longitude)
import requests
import json
"""apiadd=requests.get("http://api.airvisual.com/v2/nearest_city?lat=26.8717&lon=81.0729&key=ba3a884e-9835-4c7b-bfe5-b5965d9b0dae")
apiadd.raise_for_status()
#api = json.loads(apiadd.data)
#print(api)"""
import requests
from requests.exceptions import HTTPError

try:
    response = requests.get("http://api.airvisual.com/v2/nearest_city?lat=26.8717&lon=81.0729&key=ba3a884e-9835-4c7b-bfe5-b5965d9b0dae")
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse["data"]["current"]["pollution"]["aqius"])

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')