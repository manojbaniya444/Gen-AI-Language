from flask import Flask, render_template, request, jsonify

from lang_app import get_summary

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    person_info, profile_url = get_summary(name = name)
    
    return jsonify(
        {
            "summary": person_info.summary,
            "facts": person_info.facts,
            "topics_of_interest": person_info.topics_of_interest,
            "ice_breaker": person_info.ice_breaker,
            "profile_url": profile_url
        }
    )
    
if __name__ == "__main__":
    app.run(debug=True)