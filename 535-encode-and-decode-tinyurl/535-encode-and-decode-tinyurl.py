class Codec:
    def __init__(self):
        self.map = {}
        self.counter = 0
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.counter += 1
        self.map[self.counter] = longUrl
        return "http://tinyurl.com/"+str(self.counter)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        shortUrl = shortUrl.split("/")
        return self.map[int(shortUrl[-1])]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))