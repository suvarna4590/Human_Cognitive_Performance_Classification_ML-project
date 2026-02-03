### Project Overview:
This project focuses on predicting human cognitive performance using machine learning based on lifestyle, behavioral, and cognitive factors.
A trained LightGBM classification model is deployed using a Streamlit web application, allowing users to input details and receive real-time predictions.
The cognitive performance is classified into three levels:
- High->2
- Medium->1
- Low->0
### Objectives
- Analyze factors affecting human cognitive performance
- Build and train a robust ML classification model
- Deploy the trained model as an interactive web application
- Provide an intuitive UI for real-time predictions
### Dataset Description
The dataset contains lifestyle and cognitive-related attributes such as:
- Age
- Gender
- Sleep Duration
- Stress Level
- Diet Type
- Daily Screen Time
- Exercise Frequency
- Caffeine Intake
- Reaction Time
- Memory Test Score
These features are used to predict the overall cognitive performance level.
### Machine Learning Model
- Algorithm: LightGBM Classifier
- Problem Type: Multi-class classification
- Target Variable: Cognitive Performance Level
### Technologies Used
- Python,NumPy,Pandas,Scikit-learn,LightGBM,Streamlit,Pickle
### Web Application (Streamlit)
The Streamlit app provides:
- Input fields in the sidebar
- Scrollable table showing entered input details
- Real-time prediction results in the main panel
