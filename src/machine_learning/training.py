# src/machine_learning/training.py
from .model import MLModel
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np  # Assuming data handling requires NumPy

def load_data():
    # Placeholder for your actual data loading logic
    return np.random.rand(100, 10), np.random.randint(0, 2, 100)

def train_model():
    data, labels = load_data()
    if data is None or labels is None:
        raise ValueError("Data or labels cannot be None")

    if data.shape[0] != labels.size:
        raise ValueError("Mismatch between data samples and labels count")

    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.25, random_state=42)
    
    ml_model = MLModel()
    ml_model.train(X_train, y_train)
    
    predictions = ml_model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    print(f"Accuracy of the model: {accuracy:.2%}")

if __name__ == "__main__":
    try:
        train_model()
    except Exception as e:
        print(f"An error occurred: {e}")

    train_model()
