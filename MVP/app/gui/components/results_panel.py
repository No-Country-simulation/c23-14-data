# results_panel.py
"""Módulo: results_panel"""

import tkinter as tk
from tkinter import ttk

class ResultsPanel(ttk.Frame):
    """Panel de visualización de resultados."""
    
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        """Configura los componentes del panel."""
        self.prediction_label = ttk.Label(self, text="Predicción: -", font=("Arial", 12))
        self.prediction_label.pack(pady=5)
        
        self.confidence_bar = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")
        self.confidence_bar.pack(pady=5)