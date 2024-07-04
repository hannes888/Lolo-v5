from feed import Feed
from generate_articles import generate_articles
from rss_reader import get_rss_feed
from flask import Flask, render_template, request

# Initialize the Flask app
app = Flask(__name__)

# Parse rss feed
url = "https://flipboard.com/@raimoseero/feed-nii8kd0sz.rss"
first_feed = Feed(get_rss_feed(url=url))
feeds = [first_feed]
current_feed = first_feed

# @app.before_request
# def before_request():
#     if 'feeds' not in g:
#         feeds = [first_feed]


# Create article objects for home page
articles = generate_articles(first_feed)


@app.route('/')
def index():
    return render_template(
        'news_feed.html',
        articles=articles,
        feeds=feeds,
        big_title=first_feed.title,
        current_feed=first_feed
    )


@app.route('/save_feed', methods=['POST'])
def save_value():
    # Get the value from the form data
    input_url = request.form.get('value')
    new_feed = Feed(get_rss_feed(url=input_url))
    # Add the value to the list
    if add_feed_to_feeds(new_feed):
        # Return a success response
        return new_feed.title, 200
    else:
        return "", 500


@app.route('/view_feed', methods=['POST', 'GET'])
def view_feed():
    global current_feed

    feed_title = request.form.get('feed_title')
    # Find the clicked feed
    clicked_feed = None
    for feed in feeds:
        if feed.title == feed_title:
            clicked_feed = feed

    if clicked_feed is not None:
        # Generate new articles from the clicked feed
        global articles
        articles = generate_articles(clicked_feed)
    else:
        articles = generate_articles(first_feed)
    # Render the template with the new articles
    if clicked_feed is None:
        return render_template(
            'news_feed.html',
            articles=articles,
            feeds=feeds,
            big_title=first_feed.title,
            current_feed=first_feed
        )

    current_feed = clicked_feed

    return render_template(
        'news_feed.html',
        articles=articles,
        feeds=feeds,
        big_title=feed_title,
        current_feed=clicked_feed
    )


@app.route("/delete_feed", methods=['POST'])
def delete_feed():
    feed_title = request.form.get('feed_title')
    feeds[:] = [feed for feed in feeds if feed.title != feed_title]
    return render_template('news_feed.html',
                           articles=articles,
                           feeds=feeds,
                           big_title=feed_title,
                           current_feed=first_feed)


@app.route("/change_feed_title", methods=['POST'])
def change_feed_title():
    # Get the JSON data sent in the POST request
    data = request.get_json()

    # Access the 'original_title' and 'new_title' values
    original_title = data['original_title']
    new_title = data['new_title']

    for feed in feeds:
        if feed.title == new_title:
            return "Title already exists", 500
        if feed.title == original_title:
            feed.title = new_title

    return new_title, 200


@app.route('/filter_by_category', methods=['POST'])
def filter_by_category():
    global articles
    selected_category = request.form.get('category').upper()

    articles = [article for article in current_feed.articles if article.category.upper() == selected_category]

    return render_template('articles.html', articles=articles)


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
