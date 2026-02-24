from flask import Blueprint, render_template, request
from backend.analyzer.engine import analyze_url

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        url = request.form.get("url")

        if url:
            if not url.startswith("http"):
                url = "https://" + url

            result = analyze_url(url)

    return render_template("CYBERFLUX.html", result=result)


@main.route("/about")
def about():
    return render_template("about.html")


@main.route("/research")
def research():
    return render_template("research.html")


@main.route("/contact")
def contact():
    return render_template("contact.html")
