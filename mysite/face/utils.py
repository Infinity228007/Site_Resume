import base64


class URLShortener:
    def __init__(self):
        self.urls = {}

    def shorten_url(self, long_url):
        encoded_url = base64.b64encode(long_url.encode()).decode()
        short_url = encoded_url[:6]
        self.urls[short_url] = long_url
        return short_url

    def expand_url(self, short_url):
        long_url = self.urls.get(short_url)
        return long_url
