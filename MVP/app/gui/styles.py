# styles.py
"""Módulo: styles - Estilos CSS para EstefanIA."""

import customtkinter as ctk

# Configuración de tema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

STYLES = {
    "title": {
        "font": ("Arial", 22, "bold"),
        "text_color": "#FFFFFF",
    },
    "label": {
        "font": ("Arial", 14),
        "text_color": "#E0E0E0",
    },
    "entry": {
        "fg_color": "#263238",  # Más oscuro para contraste
        "text_color": "#E0E0E0",
        "border_color": "#546E7A",
        "width": 200,
    },
    "combo": {
        "fg_color": "#37474F",
        "text_color": "#E0E0E0",
        "dropdown_fg_color": "#263238",
        "dropdown_text_color": "#E0E0E0",
    },
    "checkbox": {
        "text_color": "#E0E0E0",
        "fg_color": "#1E88E5",  # Azul clínico
    },
    "button": {
        "fg_color": "#2E7D32",  # Verde clínico
        "hover_color": "#1B5E20",
        "text_color": "#FFFFFF",
        "font": ("Arial", 14, "bold"),
    },
    "button_danger": {
        "fg_color": "#C62828",  # Rojo alerta
        "hover_color": "#B71C1C",
        "text_color": "#FFFFFF",
        "font": ("Arial", 14, "bold"),
    },
    "frame": {
        "fg_color": "#102A43",  # Azul más oscuro para reducir brillo
    },
    "accordion": {
        "fg_color": "#235784"
    },
    "prediction": {
        "0": {
            "fg_color": "#2E7D32",  # Alta a domicilio → Verde
            "text_color": "#FFFFFF",
        },
        "1": {
            "fg_color": "#F57C00",  # Referencia hospitalaria → Naranja
            "text_color": "#FFFFFF",
        },
        "2": {
            "fg_color": "#D32F2F",  # Fallecimiento → Rojo
            "text_color": "#FFFFFF",
        },
    },
}
