# se ejecuta con streamlit run src/apppablo.py
# Se ejecuta con: streamlit run src/apppablo.py

import streamlit as st
import pandas as pd
from pickle import load
from sklearn.preprocessing import LabelEncoder


# Cargar el modelo
from joblib import load
model = load("/workspaces/c23-14-data/Models/Model_RF.sav")

# Título
st.title('Predicción de Motivo de Alta Hospitalaria')

# Subir archivo Excel o CSV
uploaded_file = st.file_uploader("Subir archivo", type=["xlsx", "csv"])

if uploaded_file is not None:
    # Leer el archivo según su extensión
    if uploaded_file.name.endswith(".xlsx"):
        df_original = pd.read_excel(uploaded_file)
    elif uploaded_file.name.endswith(".csv"):
        df_original = pd.read_csv(uploaded_file)

    # Copiar el dataframe original para trabajar con él sin modificarlo
    df = df_original.copy()

    # Normalizar nombres de columnas (eliminar espacios, convertir a minúsculas)
    df.columns = df.columns.str.strip()

    # Mostrar el contenido del archivo
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
        df_modelo = df[features].copy()

        # Transformar columnas categóricas con Label Encoding
        label_encoders = {}
        categorical_columns = ['Género', 'Residencia', 'Tipo de Admisión']
        for col in categorical_columns:
            le = LabelEncoder()
            df_modelo[col] = le.fit_transform(df_modelo[col])
            label_encoders[col] = le

        # Hacer predicciones
        predictions = model.predict(df_modelo)

        # Agregar las predicciones al dataframe original
        df_original["Predicción"] = predictions
        df_original["Predicción"] = df_original["Predicción"].map({
            0: "Motivo de Alta: Alta contra el juicio del facultativo",
            1: "Motivo de Alta: Salud Plena",
            2: "Motivo de Alta: Fallecido"
        })

        # Mostrar las predicciones junto con los datos originales
        st.subheader("Predicciones:")
        st.write(df_original)

