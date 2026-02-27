import requests
import os

CRICKET_HOST = os.getenv("CRICKET_API_HOST")
CRICKET_KEY = os.getenv("CRICKET_API_KEY")

HEADERS = {
    "X-RapidAPI-Key": CRICKET_KEY,
    "X-RapidAPI-Host": CRICKET_HOST
}

def fetch_points_table():
    url = f"https://{CRICKET_HOST}/fixtures/points-table"
    res = requests.get(url, headers=HEADERS)
    return res.json()

def fetch_match_results():
    url = f"https://{CRICKET_HOST}/fixtures/results"
    res = requests.get(url, headers=HEADERS)
    return res.json()

def fetch_match_info(match_id):
    url = f"https://{CRICKET_HOST}/fixtures/match-info?matchId={match_id}"
    res = requests.get(url, headers=HEADERS)
    return res.json()
