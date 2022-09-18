from urllib import request
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
        pass 