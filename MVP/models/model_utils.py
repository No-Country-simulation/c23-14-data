# model_utils.py

import joblib

def load_model():
    """Carga el modelo entrenado de EstefanIA."""
    try:
        model = joblib.load("/workspaces/c23-14-data/MVP/models.sav", 'rb')
        print("Modelo cargado exitosamente.")
        return model
    except Exception as e:
        print(f"Error cargando el modelo: {e}")
        raise