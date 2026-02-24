import socket
import requests


def check(url):
    try:
        # Remove http/https if present
        domain = url.replace("http://", "").replace("https://", "").split("/")[0]

        ip = socket.gethostbyname(domain)

        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = response.json()

        return {
            "ip": ip,
            "isp": data.get("isp"),
            "org": data.get("org"),
            "asn": data.get("as"),
            "country": data.get("country")
        }

    except Exception as e:
        return {"error": str(e)}
