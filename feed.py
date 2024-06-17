"""Class for storing feed data."""
from feed_types import FeedType


class Feed:
    """Feed class."""
    def __init__(self, feed, category=FeedType.News):
        self.feed = feed
        self.title = feed.feed.title
        self.link = feed.feed.link
        self.category = category
        self.entries = feed.entries
