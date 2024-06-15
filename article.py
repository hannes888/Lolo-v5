"""Class for storing article data."""


class Article:
    """Article class."""
    def __init__(self, title, summary, link, published_date, media_content=None):
        self.title = title
        self.summary = summary
        self.media_content = media_content
        self.link = link
        self.published_date = published_date
