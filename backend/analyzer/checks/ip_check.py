import re

def check(url):
    pattern = r"\d+\.\d+\.\d+\.\d+"
    if re.search(pattern, url):
        return 3
    return 0
