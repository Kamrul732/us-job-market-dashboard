import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BLS_API_KEY")

SERIES = {
    "unemployment_rate": "LNS14000000",
    "nonfarm_payrolls": "CES0000000001",
    "labor_force_participation": "LNS12300000",
    "employment_cost_index": "CIU1010000000000A"
}

def fetch_series(start_year="2014", end_year="2024"):
    url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"

    payload = {
        "seriesid": list(SERIES.values()),
        "startyear": start_year,
        "endyear": end_year,
        "registrationkey": API_KEY
    }

    response = requests.post(url, json=payload)
    data = response.json()

    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/bls_raw.json", "w") as f:
        json.dump(data, f, indent=2)

    print("✅ Data saved to data/raw/bls_raw.json")
    return data

if __name__ == "__main__":
    fetch_series()