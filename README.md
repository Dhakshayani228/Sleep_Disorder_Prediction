# Sleep Disorder Prediction Using Machine Learning 

This project is a web-based application that predicts potential sleep disorders based on user input. Built using machine learning models and a user-friendly front-end interface, the tool aims to assist users in identifying symptoms of sleep disorders and promoting better health awareness.

## Features

- Predict sleep disorders based on user data (age, BMI, heart rate, etc.)
- Interactive web interface for easy use
- Trained ML model for accurate predictions
- Clean and responsive design using HTML, CSS, and JavaScript
- Backend powered by Python and Flask

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Model:** Trained with health-related datasets

---

## Installation

Follow these steps to install and run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/Dhakshayani228/Sleep_Disorder_Prediction.git
cd Sleep_Disorder_Prediction
```

### 2. Set Up Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If there's no `requirements.txt`, install manually:

```bash
pip install flask pandas numpy scikit-learn
```

### 4. Run the Flask App

```bash
python app.py
```

### 5. Access the App

Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## How It Works

1. The user fills in the form with personal and health data.
2. The form sends this data to the Flask backend.
3. The backend uses a trained ML model to make a prediction.
4. The result (sleep disorder type or normal) is shown to the user.

---

## Project Structure

```
Sleep_Disorder_Prediction/
│
├── static/                  # CSS, JS, and images
├── templates/               # HTML templates
├── model/                   # ML model and data files
├── app.py                   # Main Flask application
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## Future Improvements

- Improve model accuracy with a larger dataset
- Add user authentication and report history
- Deploy on cloud platforms like Heroku or Render

---

## Author

**Dhakshayani Gaddam**  
Final Year B.E. Student | ML & Web Dev Enthusiast  
[LinkedIn](https://www.linkedin.com/in/dhakshayani-gaddam/) | [GitHub](https://github.com/Dhakshayani228)

---
