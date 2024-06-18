"""Class for storing feed data."""
from feed_types import FeedType
from generate_articles import generate_articles


class Feed:
    """Feed class."""
    next_id = 0

    def __init__(self, feed, category=FeedType.News):
        self.feed = feed
        self.title = feed.feed.title
        self.link = feed.feed.link
        self.category = category
        self.entries = feed.entries
        self.articles = generate_articles(feed)
        self.id = self.get_next_id()

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id
