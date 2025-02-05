# prediction_ctl.py
"""Módulo: prediction_ctl - Controlador de predicciones para EstefanIA."""

from models.model_utils import load_model

class PredictionController:
    """Controlador para manejar predicciones."""
    
    def __init__(self):
        self.model = load_model()
    
    def predict(self, input_data):
        """Ejecuta una predicción con el modelo."""
        try:
            # Convertir los datos de entrada al formato correcto
            formatted_data = [
                int(input_data["ADMISION"]),
                int(input_data["Edad"]),
                int(input_data["Género"]),
                # ... Repite para todas las características ...
                int(input_data["Embolia Pulmonar"]),
                int(input_data["Infección Torácica"])
            ]
            
            # Obtener la predicción y las probabilidades
            prediction = self.model.predict([formatted_data])[0]
            probabilities = self.model.predict_proba([formatted_data])[0]
            
            # Mapear la predicción a un resultado legible
            result_map = {0: "No Alta", 1: "Alta Parcial", 2: "Alta Completa"}
            result = result_map.get(prediction, "Desconocido")
            
            # Obtener la confianza (probabilidad máxima)
            confidence = probabilities.max() * 100  # Convertir a porcentaje
            
            return result, confidence
        except Exception as e:
            print(f"Error en la predicción: {e}")
            return "Error", 0.0