import idna
from urllib.parse import urlparse

def check(url):
    parsed = urlparse(url)
    domain = parsed.netloc

    try:
        encoded = idna.encode(domain).decode()
        if encoded != domain:
            return 3
    except:
        return 0

    return 0
