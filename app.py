from flask import Flask, render_template, request

app = Flask(__name__)

def detect_review(review):
    fake_words = ["buy now", "amazing", "best ever", "guaranteed"]

    for word in fake_words:
        if word in review.lower():
            return "⚠ Fake Review Detected"

    return "✅ Genuine Review"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    review = request.form["review"]
    result = detect_review(review)
    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)