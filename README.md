⚡ Electricity Overuse Prediction (Production ML Project)
Use this link to use the model- https://electricity-overuse-predictor.streamlit.app/

📌 Overview

An end-to-end machine learning system that predicts electricity overuse risk from daily household appliance usage and regional electricity data. The model outputs a probability score and is deployed as a live Streamlit application.

🎯 Objective 

Predict whether a household will overuse electricity based on daily usage patterns to enable proactive energy management.

🧠 Dataset 

Each record represents one day of usage,
fan, refrigerator, ac, lights, others → daily usage (hours) 
state, electricity_company → regional billing context
Target overuse (1 = overuse, 0 = normal)

🔍 EDA Highlights 

AC usage is the dominant driver of overuse risk 
Fans & refrigerators act as baseline consumption 
Regional factors influence billing sensitivity 
Model behavior aligns with real-world electricity physics

🛠 Feature Engineering & Preprocessing 

Converted all appliance usage to daily hours (user-aligned input) 
Removed leakage variables (electricity bill not used as a feature)
ColumnTransformer: 
StandardScaler → numerical features 
OneHotEncoder → categorical features
Entire preprocessing + model packaged as a single pipeline

🤖 Models Trained 

Logistic Regression Baseline, interpretable, probabilistic 
Random Forest Non-linear benchmark

📈 Model Evaluation Metrics

Accuracy, ROC-AUC, Classification Report

🚀 Deployment 

Model serialized as a pickle pipeline 
Deployed using Streamlit Hosted on Streamlit Cloud (24×7 access) 
User Input →daily appliance usage (hours) 
Model Output→probability of electricity overuse 

🔬 Technical Validation Sensitivity testing confirms

AC usage has the strongest marginal impact 
Other appliances provide contextual influence 
Model decisions are data-driven and explainable

Author: Hirak Bala
