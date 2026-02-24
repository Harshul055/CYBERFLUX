import json
import urllib.request

def check(ip):
    try:
        with urllib.request.urlopen(f"http://ip-api.com/json/{ip}") as response:
            data = json.loads(response.read().decode())

            return {
                "country": data.get("country"),
                "city": data.get("city")
            }
    except:
        return {"error": "Geo lookup failed"}
