from datetime import datetime

from article import Article
from rss_reader import get_rss_feed
from flask import Flask, render_template, request

# Initialize the Flask app
app = Flask(__name__)

# Configure the app, e.g., from a config file or environment variables
# app.config.from_object('config.DevelopmentConfig')

# Parse rss feed
url = "https://flipboard.com/@raimoseero/feed-nii8kd0sz.rss"
feed = get_rss_feed(url=url)

# for entry in feed.entries:
#     print(entry.published)


feeds = []


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
articles = generate_articles(feed)


@app.route('/')
def index():
    return render_template('news_feed.html', articles=articles)


@app.route('/save_value', methods=['POST'])
def save_value():
    # Get the value from the form data
    value = request.form.get('value')
    # Add the value to the list
    feeds.append(value)
    # Return a success response
    print(feeds)
    return '', 200


# Add more routes here

if __name__ == "__main__":
    app.run()
