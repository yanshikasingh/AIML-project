 SiteShield – Fake Website Detection using Machine Learning

Project Purpose

SiteShield is a Machine Learning–based system that determines whether a website is **real (legitimate)** or **fake (phishing)**.  
The application is deployed using Streamlit and runs directly from the command line.

What This Project Does
- Accepts website feature inputs
- Uses a trained Random Forest ML model
- Classifies websites as:
  -  Legitimate (Safe)
  -  Phishing / Fake
- Displays the prediction through a Streamlit web interface


Dataset Used
The model is trained on a phishing website dataset containing:
- URL-based features (length, symbols, IP usage, prefixes/suffixes)
- Domain-based features (DNS record, HTTPS presence)
- Content and behavior-based features (redirects, forms, scripts)


Dataset Sources:
- Kaggle Phishing Website Dataset
- PhishTank / OpenPhish (reference sources)



Folder Structure
AIML-project/
│
├── app.py
├── siteshield_model.pkl
├── siteshield_scaler.pkl
├── siteshield_feature_cols.pkl
└── README.md


File Details
- app.py 
  Streamlit application file that loads the trained model and provides a UI for prediction.

- siteshield_model.pkl 
  Trained Random Forest model.

- siteshield_scaler.pkl
  Feature scaler used during training.

- siteshield_feature_cols.pkl
  Stores feature order for correct prediction.



Technologies Used
- Python
- Streamlit
- Machine Learning (Random Forest)
- Scikit-learn
- NumPy



How to Run the Project
--bash
-pip install streamlit numpy scikit-learn
-streamlit run app.py

**Author**
**Yanshika singh**
