import os

WATCH_DIRECTORY = os.getenv("WATCH_DIRECTORY")
OUTPUT_DIRECTORY = os.getenv("OUTPUT_DIRECTORY")
SCAN_URL = os.getenv("SCAN_URL")
HEADERS = {
    "x-apikey": os.getenv("API_KEY")
}
