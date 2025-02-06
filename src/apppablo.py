# se ejecuta con streamlit run src/apppablo.py
# Se ejecuta con: streamlit run src/apppablo.py

import streamlit as st
import pandas as pd
from pickle import load

# Cargar el modelo
from joblib import load
model = load("/workspaces/c23-14-data/Models/Model_RF.sav")
# Título
st.title('Predicción de Motivo de Alta Hospitalaria')

# Subir archivo Excel
uploaded_file = st.file_uploader("Subir archivo Excel", type=["xlsx"])

if uploaded_file is not None:
    # Leer el archivo Excel
    df = pd.read_excel(uploaded_file)

    # Normalizar nombres de columnas (eliminar espacios, convertir a minúsculas)
    df.columns = df.columns.str.strip()

    # Mostrar el contenido del archivo Excel
    st.subheader("Datos cargados:")
    st.write(df.head())

    # Definir las columnas esperadas por el modelo
    features = ['Edad', 'Género', 'Residencia', 'Tipo de Admisión', 'Fumador',
                'Alcohol', 'Diabetes Mellitus', 'Hipertensión',
                'Enfermedad Coronaria Arterial', 'Miocardiopatía',
                'Enfermedad Renal Crónica', 'Anemia Severa', 'Anemia', 'Angina Estable',
                'Síndrome Coronario Agudo', 'Infarto de Miocardio(STEMI)',
                'Dolor Torácico Atípico', 'Insuficiencia Cardíaca',
                'Insuficiencia Cardíaca con Fracción de Eyección Reducida',
                'Insuficiencia Cardíaca con Fracción de Eyección Normal',
                'Enfermedad Valvular Cardíaca', 'Bloqueo Cardíaco Completo',
                'Síndrome del Nodo Sinusal Enfermo', 'Lesión Renal Aguda',
                'Accidente Cerebrovascular Isquémico',
                'Accidente Cerebrovascular Hemorrágico', 'Fibrilación Auricular',
                'Taquicardia Ventricular', 'Taquicardia Supraventricular Paroxística',
                'Cardiopatía Congénita', 'Infección del Tracto Urinario',
                'Síncope Neurocardiogénico', 'Ortostático', 'Endocarditis Infecciosa',
                'Trombosis Venosa Profunda', 'Choque Cardiogénico', 'Shock',
                'Embolia Pulmonar', 'Infección Torácica']

    # Verificar si faltan columnas en el archivo subido
    missing_columns = [col for col in features if col not in df.columns]
    if missing_columns:
        st.error(f"⚠️ Falta(n) las siguientes columnas en el archivo subido: {missing_columns}")
    else:
        st.success("✅ Todas las columnas necesarias están presentes.")

        # Filtrar solo las columnas necesarias para evitar errores
        df = df[features]

        # Hacer predicciones
        predictions = model.predict(df)

        # Mapear resultados de la predicción a texto
        df["Predicción"] = predictions
        df["Predicción"] = df["Predicción"].map({
            0: "Motivo de Alta: Alta contra el juicio del facultativo",
            1: "Motivo de Alta: Salud Plena",
            2: "Motivo de Alta: Fallecido"
        })

        # Mostrar las predicciones
        st.subheader("Predicciones:")
        st.write(df)
