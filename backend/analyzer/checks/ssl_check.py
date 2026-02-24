import ssl
import socket
from urllib.parse import urlparse

def check(url):
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.replace("www.", "")

        context = ssl.create_default_context()

        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

                return {
                    "issuer": dict(x[0] for x in cert["issuer"]),
                    "expiry_date": cert.get("notAfter")
                }
    except:
        return {"error": "SSL check failed"}
