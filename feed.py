"""Class for storing feed data."""
from generate_articles import generate_articles


class Feed:
    """Feed class."""
    next_id = 0

    def __init__(self, feed):
        self.feed = feed
        try:
            self.title = feed.feed.title
        except AttributeError:
            self.title = "Title not found"
        self.link = feed.feed.link
        self.entries = feed.entries
        self.articles = generate_articles(feed)
        self.id = self.get_next_id()
        self.categories = []

        # Get the categories from the articles and sort them
        for article in self.articles:
            if article.category:
                category = article.category.upper().strip()
                if category not in self.categories:
                    self.categories.append(category)
        self.categories.sort()

    @classmethod
    def get_next_id(cls):
        """Get the next id for the feed."""
        cls.next_id += 1
        return cls.next_id
