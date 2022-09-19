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
        steps = []

        params = {"from": origin, "to": destination}
        json = self.get_request("directions/v2/route", params)

        # handling if there was an error in get_request
        if "error" in json:
            return ["ERROR"]

        raw_steps = json["route"]["legs"][0]["maneuvers"]

        for raw_step in raw_steps:
            steps.append(raw_step["narrative"])

            
        return steps


    def print_steps(self, steps: list) -> None:
        """
        Takes steps returned by search() and prints them to console
        """
        for index, step in enumerate(steps):
            print("{}. {}".format(index + 1, step))


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

    steps = map_quest_client.search_for_steps('Clarendon Blvd,Arlington,VA', '2400+S+Glebe+Rd,+Arlington,+VA')

    map_quest_client.print_steps(steps)



  

