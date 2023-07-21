from data_manager import DataManager
import requests

KIWI_ENDPOINT = "https://tequila-api.kiwi.com"
KIWI_API = "YD03_zrm9np_9OD5vfO8nlLgjfOzmrWL"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name):
        headers = {
            "apikey": KIWI_API
        }
        query = {
            "term": f"{city_name}",
            "location_types": "city"
        }
        location_endpoints = f"{KIWI_ENDPOINT}/locations/query"
        response = requests.get(url=location_endpoints, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
