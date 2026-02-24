def check(url):
    keywords = ["login", "verify", "update", "bank", "secure"]

    for word in keywords:
        if word in url.lower():
            return 2

    return 0
