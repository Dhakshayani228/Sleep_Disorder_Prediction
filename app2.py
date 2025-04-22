from flask import Flask, render_template, request

app = Flask(__name__)

def sleep_disorder_prediction(age, gender, sleep_duration, shift_type):
    """Predict sleep disorder based on user input, including retired/unemployed."""

    shift_type = shift_type.lower()

    if shift_type == "night shift" and sleep_duration < 6:
        prediction = "Insomnia"
        confidence = "85%"
    elif age > 60 and shift_type in ["retired", "unemployed"] and sleep_duration < 6:
        prediction = "Sleep Apnea"
        confidence = "88%"
    elif age > 40 and sleep_duration < 6:
        prediction = "Sleep Apnea"
        confidence = "90%"
    elif 7 <= sleep_duration <= 9:
        prediction = "Healthy"
        confidence = "95%"
    else:
        prediction = "Sleep Irregularity"
        confidence = "75%"

    disorder_info = {
        "Healthy": {
            "reason": "No disorder detected.",
            "solution": "Maintain a healthy lifestyle.",
            "note": ""
        },
        "Insomnia": {
            "reason": "Difficulty falling or staying asleep due to stress, night shifts, or poor sleep habits.",
            "solution": "Try relaxation techniques, establish a bedtime routine, and consult a healthcare provider if needed.",
            "note": "⚠️ If symptoms persist, please consult a doctor."
        },
        "Sleep Apnea": {
            "reason": "Interrupted breathing during sleep caused by airway blockage or other health conditions.",
            "solution": "Maintain a healthy weight, avoid alcohol, and consider using a CPAP machine or consulting a sleep specialist.",
            "note": "⚠️ If symptoms persist, please consult a doctor."
        },
        "Sleep Irregularity": {
            "reason": "Your sleep pattern is irregular but does not strongly indicate a disorder.",
            "solution": "Consider improving sleep habits and monitoring for further symptoms.",
            "note": "⚠️ If issues persist, consult a specialist."
        }
    }

    return {
        "prediction": prediction,
        "confidence": confidence,
        "reason": disorder_info[prediction]["reason"],
        "solution": disorder_info[prediction]["solution"],
        "note": disorder_info[prediction]["note"]
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    age = int(request.form["age"])
    gender = request.form["gender"]
    sleep_duration = float(request.form["sleep_duration"])
    shift_type = request.form["shift_type"]

    result = sleep_disorder_prediction(age, gender, sleep_duration, shift_type)

    return render_template("index.html", **result)

if __name__ == "__main__":
    print("🚀 Flask app is running at http://127.0.0.1:5000/")
    app.run(debug=True)
