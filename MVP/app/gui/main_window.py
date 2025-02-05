import customtkinter as ctk
from config.grupos_funcionales import grupos_funcionales
from app.controllers.prediction_ctl import PredictionController
from app.gui.styles import STYLES


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EstefanIA - Predicción de Altas Médicas")
        self.geometry("1200x800")
        self.configure(fg_color=STYLES["frame"]["fg_color"])

        self.controller = PredictionController()
        self.inputs = {}
        self.prediction_var = ctk.StringVar(value="Esperando datos...")

        self.setup_ui()

    def setup_ui(self):
        """Configura la interfaz gráfica."""
        self.main_frame = ctk.CTkScrollableFrame(self, **STYLES["frame"])
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(self.main_frame, text="Formulario Clínico - EstefanIA", **STYLES["title"]).pack(pady=20)

        for group_name, features in grupos_funcionales.items():
            self.add_accordion_section(group_name, features)

        # Sección adicional "ADMISION" (entero)
        self.add_accordion_section("ADMISION", ["ADMISION"])

        self.predict_button = ctk.CTkButton(
            self.main_frame, text="Predecir Alta Médica", command=self.make_prediction, **STYLES["button"]
        )
        self.predict_button.pack(pady=20)

        # Sección de resultados
        self.result_frame = ctk.CTkFrame(self.main_frame, fg_color="#102A43")
        self.result_frame.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(self.result_frame, text="Resultado de la Predicción:", **STYLES["label"]).pack(pady=5)
        self.result_label = ctk.CTkLabel(self.result_frame, textvariable=self.prediction_var, **STYLES["title"])
        self.result_label.pack(pady=10)

    def add_accordion_section(self, title, features):
        """Crea una sección colapsable."""
        accordion = ctk.CTkFrame(self.main_frame, **STYLES["accordion"])
        accordion.pack(fill="x", pady=5, padx=10)

        content_frame = ctk.CTkFrame(accordion, fg_color="transparent")
        content_frame.pack(fill="x", padx=20, pady=10)
        content_frame.pack_forget()  # Ocultar por defecto

        accordion_header = ctk.CTkButton(
            accordion,
            text=title,
            command=lambda: self.toggle_frame(content_frame),
            fg_color=STYLES["accordion"]["fg_color"]
        )
        accordion_header.pack(fill="x")

        for i, feature in enumerate(features):
            row, col = divmod(i, 2)
            frame = ctk.CTkFrame(content_frame, fg_color="transparent")
            frame.grid(row=row, column=col, padx=10, pady=5, sticky="w")

            if feature == "Edad" or feature == "ADMISION":
                self.inputs[feature] = self.add_numeric_entry(frame, feature)
            elif feature in ["Género", "Residencia", "Tipo de Admisión"]:
                self.inputs[feature] = self.add_combo_box(frame, feature)
            else:
                self.inputs[feature] = self.add_checkbox(frame, feature)

    def toggle_frame(self, frame):
        """Muestra u oculta el contenido de una sección"""
        if frame.winfo_ismapped():
            frame.pack_forget()
        else:
            frame.pack(fill="x", expand=True)

    def make_prediction(self):
        """Obtiene datos de entrada y hace una predicción."""
        input_data = {}
        for feature, widget in self.inputs.items():
            if isinstance(widget, ctk.IntVar):
                input_data[feature] = widget.get()
            elif isinstance(widget, ctk.CTkComboBox):
                input_data[feature] = widget.get()
            else:
                try:
                    input_data[feature] = int(widget.get()) if widget.get().isdigit() else 0
                except ValueError:
                    input_data[feature] = 0

        prediction = self.controller.predict(input_data)
        self.update_prediction_display(prediction)

    def update_prediction_display(self, prediction):
        """Actualiza la UI con la predicción y colores adecuados."""
        prediction_texts = ["Alta a domicilio", "Referencia hospitalaria", "Fallecimiento"]
        self.prediction_var.set(f"Resultado: {prediction_texts[prediction]}")

        self.result_label.configure(
            fg_color=STYLES["prediction"][str(prediction)]["fg_color"],
            text_color=STYLES["prediction"][str(prediction)]["text_color"]
        )

    def add_checkbox(self, parent, feature):
        """Checkbox para variables booleanas."""
        var = ctk.IntVar(value=0)
        checkbox = ctk.CTkCheckBox(parent, text=feature.replace("_", " "), variable=var, **STYLES["checkbox"])
        checkbox.pack(anchor="w")
        return var

    def add_combo_box(self, parent, feature):
        """Combobox para variables categóricas."""
        options = {
            "Género": ["Masculino", "Femenino"],
            "Residencia": ["Urbana", "Rural"],
            "Tipo de Admisión": ["Urgencias", "Programada"]
        }.get(feature, [])

        combo = ctk.CTkComboBox(parent, values=options, **STYLES["combo"])
        combo.pack()
        return combo

    def add_numeric_entry(self, parent, feature):
        """Campo numérico para la edad y ADMISION."""
        entry = ctk.CTkEntry(parent, **STYLES["entry"])
        entry.pack()
        return entry


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
