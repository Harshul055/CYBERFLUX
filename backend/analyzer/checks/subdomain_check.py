from urllib.parse import urlparse

def check(url):
    parsed = urlparse(url)
    domain = parsed.netloc

    parts = domain.split(".")
    
    if len(parts) > 3:
        return 2

    return 0
