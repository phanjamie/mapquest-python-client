import requests
from dotenv import load_dotenv
import os

load_dotenv()
MAPQUEST_KEY = os.getenv("MAPQUEST_KEY")
MAPQUEST_URL = os.getenv("MAPQUEST_URL")

class MapQuestClient:
    def search_for_steps(self, origin: str, destination: str) -> list:
        """
        Returns list of steps to get from origin to destination
        """
        pass


    def print_steps(self, steps: list) -> None:
        """
        Takes steps returned by search() and prints them to console
        """
        pass

    def get_request(self, route: str, params: dict):
        """
        Makes request to MapQuests api and returns encoded JSON
        """
        params["key"] = MAPQUEST_KEY

        url = MAPQUEST_URL + "/" + route

        response = requests.get(url = url, params = params)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            # handling 400s & 500s
            return { 'error': 'MapQuest API returned with status code: {}'.format(response.status_code) }

        return response.json()

        


if __name__ == "__main__":

    map_quest_client = MapQuestClient()

    params = {
        'from': 'Clarendon Blvd,Arlington,VA',
        'to': '2400+S+Glebe+Rd,+Arlington,+VA'
    }

    response = map_quest_client.get_request("directions/v2/route", params )

    print(response)