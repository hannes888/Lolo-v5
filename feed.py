"""Class for storing feed data."""
from feed_types import FeedType
from generate_articles import generate_articles


class Feed:
    """Feed class."""
    next_id = 0

    def __init__(self, feed, category=FeedType.News):
        self.feed = feed
        try:
            self.title = feed.feed.title
        except AttributeError:
            self.title = "Title not found"
        self.link = feed.feed.link
        self.category = category
        self.entries = feed.entries
        self.articles = generate_articles(feed)
        self.id = self.get_next_id()

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    def to_dict(self):
        """Return a dictionary representation of the feed object."""
        return {
            'title': self.title,
            'link': self.link,
            'category': self.category,
            'entries': self.entries,
            'articles': self.articles,
            'id': self.id
        }
