# model_utils.py

import joblib

def load_model():
    """Carga el modelo entrenado de EstefanIA."""
    try:
        model = joblib.load("models/estefania_model.pkl")
        print("Modelo cargado exitosamente.")
        return model
    except Exception as e:
        print(f"Error cargando el modelo: {e}")
        raise