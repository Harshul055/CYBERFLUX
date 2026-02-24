from backend.analyzer.checks import (
    url_length,
    https_check,
    ip_check,
    keyword_check,
    subdomain_check,
    at_symbol_check,
    hyphen_check,
    unicode_check,
    typosquat_check,
    shortener_check,
    domain_age_check,
    network_info,
    isp_lookup
)
from .scoring import calculate_risk



def analyze_url(url):

    result = {}

    #  Basic URL Checks
    result["URL Length"] = url_length.check(url)
    result["HTTPS Check"] = https_check.check(url)
    result["IP Address in URL"] = ip_check.check(url)
    result["Suspicious Keywords"] = keyword_check.check(url)
    result["Subdomain Count"] = subdomain_check.check(url)
    result["@ Symbol Check"] = at_symbol_check.check(url)
    result["Hyphen Check"] = hyphen_check.check(url)
    result["Unicode Check"] = unicode_check.check(url)
    result["Typosquatting Check"] = typosquat_check.check(url)
    result["Shortener Check"] = shortener_check.check(url)

    #  Domain + Network
    result["Domain Information"] = domain_age_check.check(url)
    result["Network Information"] = network_info.check(url)
    result["ISP Information"] = isp_lookup.check(url)

    #  Score Calculation
    score, level,confidence  = calculate_risk(result)
    result["Total Risk Score"] = score
    result["Risk Level"] = level
    result["Confidence"] = str(confidence) + "%"

    return result
