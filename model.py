import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

class SalesPrediction:

    def __init__(self, csv_file):
        self.dataset = pd.read_csv(csv_file)
        print("Dataset loaded successfully.")
        
    def preprocess_data(self):
        X = self.dataset.iloc[:, :-1].values
        y = self.dataset.iloc[:, 1].values
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=1/3, random_state=0)
        print("Data preprocessed.")
        
        sc_X = StandardScaler()
        self.X_train = sc_X.fit_transform(self.X_train)
        self.X_test = sc_X.transform(self.X_test)
        sc_y = StandardScaler()
        self.y_train = sc_y.fit_transform(self.y_train.reshape(-1, 1))
        print("Feature scaling completed.")
        
    def train_model(self):
        self.regressor = LinearRegression()
        self.regressor.fit(self.X_train, self.y_train)
        print("Model training complete.")

    def predict(self):
        self.y_pred = self.regressor.predict(self.X_test)
        print("Prediction complete.")
        
    def visualize_results(self, X, y, dataset_type):
        plt.scatter(X, y, color='red')
        plt.plot(self.X_train, self.regressor.predict(self.X_train), color='blue')
        plt.title(f'Sales vs Time ({dataset_type} set)')
        plt.xlabel('Time')
        plt.ylabel('Sales')
        plt.show()
        print(f"{dataset_type} set visualization complete.")
        
if __name__ == "__main__":
    sp = SalesPrediction('Sales_Data.csv')
    sp.preprocess_data()
    sp.train_model()
    sp.predict()
    sp.visualize_results(sp.X_train, sp.y_train, 'Training')
    sp.visualize_results(sp.X_test, sp.y_test, 'Test')
