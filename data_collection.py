import requests
import csv
import time

class PublicRecordsCollector:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.base_url = "https://api.publicrecords.example.com"  # Replace with actual API URL

    def fetch_legal_cases(self, query):
        """Fetch legal cases from a public API."""
        endpoint = f"{self.base_url}/legal_cases"
        params = {
            "query": query,
            "api_key": self.api_key
        }
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching legal cases: {e}")
            return []

    def fetch_property_records(self, location):
        """Fetch property records from a public API."""
        endpoint = f"{self.base_url}/property_records"
        params = {
            "location": location,
            "api_key": self.api_key
        }
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching property records: {e}")
            return []

    def save_to_csv(self, data, filename):
        """Save collected data to a CSV file."""
        if not data:
            print("No data to save.")
            return
        keys = data[0].keys()
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data saved to {filename}")

if __name__ == "__main__":
    collector = PublicRecordsCollector(api_key="your_api_key_here")
    legal_cases = collector.fetch_legal_cases("John Doe")
    property_records = collector.fetch_property_records("New York")
    collector.save_to_csv(legal_cases, "data/legal_cases.csv")
    collector.save_to_csv(property_records, "data/property_records.csv")
