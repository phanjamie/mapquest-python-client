from urllib import request
from dotenv import load_dotenv
import os

load_dotenv()
MAPQUEST_KEY = os.getenv("MAPQUEST_KEY")
MAPQUEST_URL = os.getenv("MAPQUEST_URL")
