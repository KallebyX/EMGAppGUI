# src/machine_learning/training.py
from .model import MLModel
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def load_data():
    # Implementar a carga de seus dados
    pass

def train_model():
    data, labels = load_data()
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.25, random_state=42)
    
    ml_model = MLModel()
    ml_model.train(X_train, y_train)
    
    predictions = ml_model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    print(f"Accuracy of the model: {accuracy:.2%}")

if __name__ == "__main__":
    train_model()
