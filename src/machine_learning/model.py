# src/machine_learning/model.py
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

class MLModel:
    def __init__(self, model_type='RandomForest', n_estimators=100):
        self.model = self.load_model(model_type, n_estimators)
        self.scaler = StandardScaler()

    def load_model(self, model_type, n_estimators):
        if model_type == 'RandomForest':
            return RandomForestClassifier(n_estimators=n_estimators)
        # Add support for more models here
        raise ValueError("Model type not supported")

    def train(self, X_train, y_train):
        X_train_scaled = self.scaler.fit_transform(X_train)
        self.model.fit(X_train_scaled, y_train)

    def predict(self, X):
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)

