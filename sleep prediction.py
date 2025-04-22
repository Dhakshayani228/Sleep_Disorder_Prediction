def sleep_disorder_prediction(age, gender, sleep_duration, shift_type):
    """Predict sleep disorder based on real-time user input, including retired individuals."""

    shift_type = shift_type.lower()
    
    # Rule-based conditions for prediction
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

    # Disorder information
    disorder_info = {
        "Healthy": {
            "reason": "No disorder detected",
            "solution": "Maintain a healthy lifestyle.",
            "note": ""
        },
        "Insomnia": {
            "reason": "Difficulty falling or staying asleep due to stress, night shifts, or poor sleep habits.",
            "solution": "Try relaxation techniques, establish a bedtime routine, and consult a healthcare provider if needed.",
            "note": " If symptoms persist, please consult a doctor."
        },
        "Sleep Apnea": {
            "reason": "Interrupted breathing during sleep caused by airway blockage or other health conditions.",
            "solution": "Maintain a healthy weight, avoid alcohol, and consider using a CPAP machine or consulting a sleep specialist.",
            "note": "If symptoms persist, please consult a doctor."
        },
        "Sleep Irregularity": {
            "reason": "Your sleep pattern is irregular but does not strongly indicate a disorder.",
            "solution": "Consider improving sleep habits and monitoring for further symptoms.",
            "note": "If issues persist, consult a specialist."
        }
    }

    return {
        "Prediction": prediction,
        "Confidence": confidence,
        "Reason": disorder_info[prediction]["reason"],
        "Solution": disorder_info[prediction]["solution"],
        "Note": disorder_info[prediction]["note"]
    }

# Real-Time User Input Simulation
print("\n Welcome to the Sleep Disorder Prediction System!")
age = int(input("Enter your age: "))
gender = input("Enter your gender (Male/Female): ").strip().capitalize()
sleep_duration = float(input("Enter your sleep duration (in hours): "))
print("Shift Type Options: Regular Job, Night Shift, Morning Shift, Retired, Unemployed")
shift_type = input("Enter your occupation type: ").strip().capitalize()

# Run Prediction
print("\n Sleep Disorder Prediction")
result = sleep_disorder_prediction(age, gender, sleep_duration, shift_type)

# Display Result
print("\n Prediction Results:")
for key, value in result.items():
    print(f"{key}: {value}")
