from urllib.parse import urlparse

def check(url):
    parsed = urlparse(url)
    domain = parsed.netloc

    shorteners = ["bit.ly", "tinyurl.com", "goo.gl"]

    for short in shorteners:
        if short in domain:
            return 2

    return 0
