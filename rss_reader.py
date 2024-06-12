from bs4 import BeautifulSoup
import requests

url = requests.get("https://flipboard.com/@raimoseero/feed-nii8kd0sz.rss")

url_webparser = "https://uptime-mercury-api.azurewebsites.net/webparser"
data = {
    "url": "https://flipboard.com/@raimoseero/feed-nii8kd0sz.rss"
}

# Send the POST request
response = requests.post(url_webparser, json=data)

# Print the response
print(response.text)

soup = BeautifulSoup(url.content, "xml")
items = soup.find_all("item")

# Loop through each item
for item in items:
    title = item.title.text
    link = item.link.text
    description = item.description.text

    print(f"Title: {title}")
    print(f"Link: {link}")
    print(f"Description: {description}")
    print("\n")
