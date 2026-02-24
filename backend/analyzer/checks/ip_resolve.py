import socket
from urllib.parse import urlparse

def check(url):
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.replace("www.", "")
        ip = socket.gethostbyname(domain)

        return {
            "domain": domain,
            "ip_address": ip
        }
    except:
        return {"error": "IP resolve failed"}
