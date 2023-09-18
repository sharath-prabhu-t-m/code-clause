import pyshorteners

class URLShortener:
    def __init__(self):
        self.shortener = pyshorteners.Shortener()
    
    def shorten_url(self, original_url):
        short_url = self.shortener.tinyurl.short(original_url)
        return short_url
    
    def expand_url(self, short_url):
        expanded_url = self.shortener.tinyurl.expand(short_url)
        return expanded_url

# Example usage
shortener = URLShortener()
original_url = "https://www.example.com"
short_url = shortener.shorten_url(original_url)
print(f"Shortened URL: {short_url}")
expanded_url = shortener.expand_url(short_url)
print(f"Expanded URL: {expanded_url}")
