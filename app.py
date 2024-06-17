from datetime import datetime

from article import Article
from feed import Feed
from feed_types import FeedType
from rss_reader import get_rss_feed
from flask import Flask, render_template, request

# Initialize the Flask app
app = Flask(__name__)


# Parse rss feed
url = "https://flipboard.com/@raimoseero/feed-nii8kd0sz.rss"
first_feed = Feed(get_rss_feed(url=url), FeedType.News)
feeds = [first_feed]


def generate_articles(rss_feed):
    """Generate a list of article objects from a feed."""
    article_objects = []

    for entry in rss_feed.entries:
        # Check for media_content
        if "media_content" in entry:
            media_content = entry.media_content
        else:
            media_content = None

        article = Article(
            title=entry.title,
            summary=entry.summary,
            link=entry.link,
            published_date=entry.published,
            media_content=media_content
        )

        article_objects.append(article)

    # Sort the articles by publishing date
    article_objects.sort(
        key=lambda article_object: datetime.strptime(
            article_object.published_date, "%a, %d %b %Y %H:%M:%S %Z"
        )
    )

    return article_objects


# Create article objects
articles = generate_articles(first_feed)


@app.route('/')
def index():
    return render_template('news_feed.html', articles=articles, feeds=feeds)


@app.route('/save_value', methods=['POST'])
def save_value():
    # Get the value from the form data
    input_url = request.form.get('value')
    new_feed = Feed(get_rss_feed(url=input_url), FeedType.News)
    # Add the value to the list
    if add_feed_to_feeds(new_feed):
        # Return a success response
        return new_feed.title, 200
    else:
        return "", 500


@app.route('/view_feed', methods=['POST'])
def view_feed():
    feed_title = request.form.get('feed_title')
    # ... your code here to handle the feed ...
    return render_template('feed_view.html', feed_title=feed_title)


def add_feed_to_feeds(feed_to_add):
    """
    Add a feed to the feeds list if it is not already present.

    :param feed_to_add: A feed object to add to the feeds list.
    :return: True if the feed was added, False otherwise.
    """
    if any(feed.link == feed_to_add.link for feed in feeds):
        return False
    feeds.append(feed_to_add)
    return True


if __name__ == "__main__":
    app.run()
