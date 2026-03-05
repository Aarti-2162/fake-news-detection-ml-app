# fake-news-detection-ml-app

This project is a Machine Learning based web application that detects whether a news article is Real or Fake.

The model is trained using Logistic Regression and TF-IDF vectorization. The web interface is built using Flask.

Users can enter any news text, and the system predicts whether it is Real News or Fake News with a confidence score.

## Technologies Used

Python  
Flask  
Scikit-learn  
TF-IDF Vectorizer  
Logistic Regression  
HTML / CSS  

## Project Structure

fake_news_detection_app
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── templates
│   └── index.html
└── README.md

## How to Run the Project

1. Clone the repository

git clone https:https://github.com/Aarti-2162/fake-news-detection-ml-app.git

2. Install dependencies

pip install flask scikit-learn

3. Run the application

python app.py

4. Open browser and go to

http://127.0.0.1:5000/

## Features

Detects fake news using machine learning  
Simple and clean user interface  
Confidence score for prediction  
Fast prediction using trained model

## Future Improvements

Add deep learning model  
Improve UI design  
Deploy the app online
