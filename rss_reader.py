import feedparser

# # Define the URL of the RSS feed
# url = "https://flipboard.com/@raimoseero/feed-nii8kd0sz.rss"
#
# # Parse the RSS feed
# feed = feedparser.parse(url)
#
#
#
# # Print the feed title
# print(f"Feed Title: {feed.feed.title}")
#
# # Print the feed link
# print(f"Feed Link: {feed.feed.link}")
#
# # Print the titles of each feed item
# for entry in feed.entries[::-1]:
#     print(f"Item Title: {entry.title}")
#     print(f"Item Link: {entry.link}")
#     print(f"Item Description: {entry.description}")
#     if "media_content" in entry:
#         print(entry.media_content)
#     print("---")


def get_rss_feed(url):
    """Get parsed rss feed from url."""
    return feedparser.parse(url)
