"""Class for storing article data."""


class Article:
    """Article class."""
    def __init__(self, title, summary, link, published_date, media_content_url=None, category=None):
        self.title = title
        self.summary = summary
        self.media_content_url = media_content_url
        self.link = link
        self.published_date = published_date
        self.category = category
