import requests
import json

# Define the API endpoint
api_url = "https://uptime-mercury-api.azurewebsites.net/webparser"

# Define the JSON body for the POST request
data = {
    "url": "https://nussknacker.io/"
}

# Send a POST request to the API
response = requests.post(api_url, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON into a Python dictionary
    feed = response.json()

    # Access data from the feed
    print(json.dumps(feed, indent=4))
    print(f"Response text: {response.text}")
else:
    print(f"Failed to get feed: {response.status_code}")
    print(f"Response text: {response.text}")