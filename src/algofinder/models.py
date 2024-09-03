import joblib
import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def load_training_data(file_path):
    data = pd.read_csv(file_path)
    X = data.drop(columns=['complexity'])
    y = data['complexity']
    return X, y

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model Mean Squared Error: {mse}")
    return model

def save_model(model, file_path):
    joblib.dump(model, file_path)

def load_model(file_path):
    if os.path.exists(file_path):
        return joblib.load(file_path)
    else:
        return None
