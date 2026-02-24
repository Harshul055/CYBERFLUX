import idna
import difflib
from urllib.parse import urlparse

# 🇮🇳 Top Indian Brands + Banks
INDIA_BRANDS = [

    # 🔹 Major Companies
    "reliance.com",
    "tcs.com",
    "infosys.com",
    "wipro.com",
    "tatamotors.com",
    "mahindra.com",
    "adityabirla.com",
    "hindustanunilever.com",
    "itcportal.com",
    "asianpaints.com",
    "godrej.com",
    "dabur.com",
    "amul.com",

    # 🔹 E-commerce & Tech
    "flipkart.com",
    "amazon.in",
    "myntra.com",
    "ajio.com",
    "bigbasket.com",
    "nykaa.com",
    "snapdeal.com",
    "indiamart.com",

    # 🔹 Travel & Services
    "makemytrip.com",
    "cleartrip.com",
    "redbus.in",
    "bookmyshow.com",
    "irctc.co.in",

    # 🔹 Telecom
    "jio.com",
    "airtel.in",
    "bsnl.co.in",

    # 🔹 Fintech
    "paytm.com",
    "phonepe.com",
    "groww.in",
    "zerodha.com",
    "upstox.com",
    "policybazaar.com",

    # 🔴 PUBLIC SECTOR BANKS
    "sbi.co.in",
    "bankofbaroda.in",
    "pnbindia.in",
    "canarabank.com",
    "unionbankofindia.co.in",
    "indianbank.in",
    "bankofindia.co.in",
    "centralbankofindia.co.in",
    "iob.in",
    "ucobank.com",

    # 🔴 PRIVATE BANKS
    "hdfcbank.com",
    "icicibank.com",
    "axisbank.com",
    "kotak.com",
    "yesbank.in",
    "idfcfirstbank.com",
    "indusind.com",
    "rblbank.com",
    "federalbank.co.in",
    "southindianbank.com",

    # 🔴 Payment Banks
    "airtelpaymentsbank.com",
    "paytmbank.com",
    "fino.bank",
    "jpbnbank.co.in"
]


def extract_domain(url):
    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    if domain.startswith("www."):
        domain = domain[4:]

    return domain


def check(url):
    domain = extract_domain(url)

    # 🔴 1️⃣ Unicode Homograph Detection
    try:
        encoded = idna.encode(domain).decode()
        if encoded != domain:
            return 3
    except:
        return 0

    # 🟠 2️⃣ Typosquat Similarity Check
    for brand in INDIA_BRANDS:
        similarity = difflib.SequenceMatcher(None, domain, brand).ratio()

        if similarity > 0.85 and domain != brand:
            return 3

    return 0
