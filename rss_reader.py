import feedparser


def get_rss_feed(url):
    """Get parsed rss feed from url."""
    return feedparser.parse(url)
