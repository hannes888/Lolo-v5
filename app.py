"""import statements"""
from flask import Flask, render_template
import feedparser
from waitress import serve


# create instance of Flask
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Endpoint for accessing the Feed data"""

    rss_news_urls = ["https://www.wired.com/feed/rss", "https://www.nsnam.org/feed.xml"]
    data = []
    for url in rss_news_urls:
        data.append(feedparser.parse(url)['entries'])

    return render_template('index.html', articles_data=data)


# Run the Flask application
if __name__ == '__main__':
    serve(app)
