# validators.py
"""Módulo: validators - Validaciones para los datos de entrada."""

def validate_integer_inputs(input_data):
    """Verifica que todos los valores sean enteros."""
    for key, value in input_data.items():
        try:
            int(value)
        except ValueError:
            raise ValueError(f"Valor inválido en {key}: '{value}' no es un entero")
    return True