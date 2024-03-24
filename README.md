# Car Price Prediction Project 🚗💰

This project focuses on predicting the selling price of cars based on various features such as the year of manufacture, present price, kilometers driven, fuel type, seller type, transmission, owner, and age of the car. The dataset used for this project is stored in the `car.csv` file.

To Access,please visit:https://carpricepredictionbilal.streamlit.app/

## Project Structure 📂

The project consists of the following files:

- `car.csv`: Dataset containing information about cars.
- `car_price_prediction.ipynb`: Jupyter Notebook containing the Python code for data preprocessing, model training, and evaluation.
- `Car_Price_Predictor.pkl`: Serialized model file containing the trained model for car price prediction.
- `README.md`: This file providing an overview of the project.

## Data Preprocessing 🛠️

- Loaded the dataset using Pandas.
- Checked for missing values and handled them appropriately.
- Created a new feature 'Age' based on the current year and the year of manufacture.
- Encoded categorical variables using label encoding.

## Model Training 🤖

- Split the data into training and testing sets using `train_test_split` from `sklearn.model_selection`.
- Trained four different regression models:
  - Linear Regression
  - Random Forest Regression
  - XGBoost Regression
  - Gradient Boosting Regression

## Model Evaluation 📊

- Evaluated the models using R-squared (coefficient of determination) metric.


## Model Deployment 🚀

- Saved the trained Regression model using joblib 
- This serialized model file can be used for making predictions on new data.

## Usage ℹ️

To use the trained model for making predictions on new data:

1. Load the serialized model using joblib or pickle.
2. Provide the required features of the car (present price, kilometers driven, fuel type, seller type, transmission, owner, and age).
3. Call the `predict` method on the loaded model to get the predicted selling price of the car.

