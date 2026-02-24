import socket
import ssl
from urllib.parse import urlparse

def check(url):
    result = {}

    try:
        parsed = urlparse(url)
        domain = parsed.netloc.replace("www.", "")

        ip = socket.gethostbyname(domain)
        result["ip_address"] = ip

        # SSL Info
        try:
            context = ssl.create_default_context()
            with socket.create_connection((domain, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    result["ssl_expiry"] = cert.get("notAfter")
        except:
            result["ssl_expiry"] = "No SSL"

        return result

    except Exception as e:
        return {"network_error": str(e)}
