# input_panel.py
"""Módulo: input_panel"""

import tkinter as tk
from tkinter import ttk

class InputPanel(ttk.Frame):
    """Panel de entrada de datos."""
    
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        """Configura los componentes del panel."""
        ttk.Label(self, text="Característica 1:").grid(row=0, column=0)
        self.feature1 = ttk.Entry(self)
        self.feature1.grid(row=0, column=1, pady=5)
        
        ttk.Label(self, text="Característica 2:").grid(row=1, column=0)
        self.feature2 = ttk.Entry(self)
        self.feature2.grid(row=1, column=1, pady=5)