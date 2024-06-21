from datetime import datetime
from article import Article


def parse_date(date_string):
    for fmt in ["%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z"]:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            pass
    raise ValueError(f"time data {date_string} does not match either of the formats %a, %d %b %Y %H:%M:%S %Z or %a, %d %b %Y %H:%M:%S %z")


def generate_articles(rss_feed):
    """Generate a list of article objects from a feed."""
    article_objects = []

    for entry in rss_feed.entries:
        # Check for media_content
        # TODO check media:thumbnail etc
        if "media_content" in entry:
            media_content_url = entry.media_content[0]["url"]
        else:
            media_content_url = None

        # Check for categories, choose the first one
        if "category" in entry:
            category = entry.category
        else:
            category = None

        # Check if link attribute exists
        link = entry.link if hasattr(entry, 'link') else 'No link provided'

        article = Article(
            title=entry.title,
            summary=entry.summary,
            link=link,
            published_date=entry.published,
            media_content_url=media_content_url,
            category=category,
        )

        article_objects.append(article)

    # Sort the articles by publishing date
    article_objects.sort(
        key=lambda article_object: parse_date(article_object.published_date)
    )

    return article_objects
