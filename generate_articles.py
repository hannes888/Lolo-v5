"""Functions for generating article objects from an RSS feed."""


from datetime import datetime
from article import Article
import requests


# Define the API endpoint
api_url = "https://uptime-mercury-api.azurewebsites.net/webparser"


def parse_date(date_string):
    """Parse a date string into a datetime object."""
    for fmt in ["%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z"]:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            pass
    raise ValueError(f"time data {date_string} does not match either of the formats")


def generate_articles(rss_feed):
    """
    Generate a list of article objects from a feed.
    :param rss_feed: An RSS feed object.
    :return: A list of sorted article objects.
    """
    article_objects = []

    for entry in rss_feed.entries:
        if hasattr(entry, 'link'):
            entry_link = entry.link

            data = {
                "url": f"{entry_link}"
            }

            # WARNING: Using the provided API significantly reduces response times
            response = requests.post(api_url, json=data)
            title = None
            summary = None
            media_content_url = None

            if response.status_code == 200:
                article_data = response.json()
                title = article_data.get("title", None)
                summary = article_data.get("excerpt", None)
                media_content_url = article_data.get("lead_image_url", None)

            # Check if article items with none value can be retrieved from the entry using feedparser instead
            if title is None:
                title = entry.title

            if summary is None:
                summary = entry.summary

            if media_content_url is None:
                if "media_content" in entry:
                    media_content_url = entry.media_content[0]["url"]
                elif "media_thumbnail" in entry:
                    media_content_url = entry.media_thumbnail[0]["url"]
                else:
                    media_content_url = None

            # Check for categories in the xml, choose the first one
            if "tags" in entry and entry.tags:
                category = entry.tags[0]['term']
            elif "category" in entry:
                category = entry.category
            else:
                category = "OTHER"

            article = Article(
                title=title,
                summary=summary,
                link=entry_link,
                published_date=entry.published,
                media_content_url=media_content_url,
                category=category
            )

            article_objects.append(article)

    # Sort the articles by publishing date
    article_objects.sort(
        key=lambda article_object: parse_date(article_object.published_date)
    )

    return article_objects
