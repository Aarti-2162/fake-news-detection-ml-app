from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form["news"]
    vector = vectorizer.transform([text])

    prediction = model.predict(vector)
    prob = model.predict_proba(vector)
    confidence = round(max(prob[0]) * 100, 2)

    if prediction[0] == 0:
        result = f"Real News ✅ ({confidence}% confident)"
    else:
        result = f"Fake News ❌ ({confidence}% confident)"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)