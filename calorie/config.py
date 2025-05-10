from dotenv import load_dotenv
import os

load_dotenv()
CALORIE_NINJAS_API_KEY = os.getenv("Key")
CALORIE_NINJAS_URL = os.getenv("Url")