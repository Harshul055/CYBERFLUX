import whois
from datetime import datetime, timezone

def check(url):
    result = {}

    try:
        domain_info = whois.whois(url)

        expiry = domain_info.expiration_date
        creation = domain_info.creation_date

        # If list returned
        if isinstance(expiry, list):
            expiry = expiry[0]
        if isinstance(creation, list):
            creation = creation[0]

        result["domain_created"] = str(creation)
        result["domain_expiry"] = str(expiry)

        # 🔥 FIX HERE
        if creation:
            if creation.tzinfo is not None:
                now = datetime.now(timezone.utc)
            else:
                now = datetime.now()

            age_days = (now - creation).days
            result["domain_age_days"] = age_days

        return result

    except Exception as e:
        return {"domain_error": str(e)}
