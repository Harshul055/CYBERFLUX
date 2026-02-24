from urllib.parse import urlparse

def check(url):
    parsed = urlparse(url)
    domain = parsed.netloc

    if domain.count("-") > 2:
        return 1

    return 0
