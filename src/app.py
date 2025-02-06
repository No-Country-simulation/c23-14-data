#recorda pip install streamlit
#recorda pip install fp
# se ejecuta con streamlit run src/app.py 
from pickle import load
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from io import BytesIO
from joblib import load
import plotly.express as px
import altair as alt
from io import BytesIO
import requests



# Cargar el modelo
from joblib import load
url = "https://github.com/No-Country-simulation/c23-14-data/raw/refs/heads/main/Models/Model_RF.sav"
response = requests.get(url)
model = load(BytesIO(response.content))

# Estilos personalizados (CSS)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f4f7;  /* Color de fondo más claro */
    }
    
    .stTitle {
        color: #2C3E50;  /* Título oscuro para mejor contraste */
        font-weight: bold;
    }

    .stExpanderHeader {
        background-color: #16A085;  /* Verde brillante para encabezados */
        color: white;
        font-size: 18px;
        font-weight: bold;
    }

    .stExpanderContent {
        background-color: #EAF0F1;  /* Fondo claro para el contenido */
    }

    .stRadio label, .stSlider label, .stCheckbox label {
        color: #1ABC9C;  /* Color vibrante para textos */
        font-size: 20px;
        font-weight: bold;
    }

    .stButton>button {
        background-color: #E74C3C;  /* Rojo brillante para el botón */
        color: white;
        font-size: 20px;
        font-weight: bold;
        padding: 15px 30px;
        border-radius: 8px;
        border: none;
        transition: background-color 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #C0392B;  /* Rojo oscuro al hacer hover */
    }

    .stText {
        color: #34495E;  /* Texto de predicción en color oscuro */
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True
)

# Título
st.title('Predicción de Motivo de Alta Hospitalaria')

# Grupo de Datos Demográficos
with st.expander("Datos Demográficos"):
    edad = st.slider("Edad", min_value=15, max_value=100, step=1)
    genero = st.radio("Género", ['Masculino', 'Femenino'])
    residencia = st.radio("Residencia", ['Urbana', 'Rural'])

# Grupo de Tipo de Admisión
with st.expander("Tipo de Admisión"):
    tipo_admision = st.radio("Tipo de Admisión", ['Emergencia', 'Ambulatoria'])

# Grupo de Hábitos y Factores de Riesgo
with st.expander("Hábitos y Factores de Riesgo"):
    fumador = st.checkbox("Fumador")
    alcohol = st.checkbox("Consumo de Alcohol")
    diabetes = st.checkbox("Diabetes Mellitus")
    hipertension = st.checkbox("Hipertensión")
    enfermedad_coronaria = st.checkbox("Enfermedad Coronaria Arterial")

# Grupo de Enfermedades Cardíacas
with st.expander("Enfermedades Cardíacas"):
    miocardiopatia = st.checkbox("Miocardiopatía")
    insuficiencia_card = st.checkbox("Insuficiencia Cardíaca")
    insuficiencia_eje_reducida = st.checkbox("Insuficiencia Cardíaca con Fracción de Eyección Reducida")
    insuficiencia_eje_normal = st.checkbox("Insuficiencia Cardíaca con Fracción de Eyección Normal")
    enfermedad_valvular = st.checkbox("Enfermedad Valvular Cardíaca")
    bloqueo_card = st.checkbox("Bloqueo Cardíaco Completo")

# Grupo de Complicaciones Agudas
with st.expander("Complicaciones Agudas"):
    sindrome_nodo_sinusal = st.checkbox("Síndrome del Nodo Sinusal Enfermo")
    lesion_renal = st.checkbox("Lesión Renal Aguda")
    accidente_cerebrovascular_isquemico = st.checkbox("Accidente Cerebrovascular Isquémico")
    fibrilacion_auricular = st.checkbox("Fibrilación Auricular")
    taquicardia_ventricular = st.checkbox("Taq. Ventricular")
    choque_cardiogenico = st.checkbox("Choque Cardiogénico")

# Grupo de Infecciones y Trombosis
with st.expander("Infecciones y Trombosis"):
    embolia_pulmonar = st.checkbox("Embolia Pulmonar")
    infeccion_toracica = st.checkbox("Infección Torácica")
    trombosis_venosa_profunda = st.checkbox("Trombosis Venosa Profunda")

# Otras condiciones
with st.expander("Otras Condiciones"):
    anemia_severa = st.checkbox("Anemia Severa")
    anemia = st.checkbox("Anemia")
    angina_estable = st.checkbox("Angina Estable")
    infarto_miocardio = st.checkbox("Infarto de Miocardio (STEMI)")
    dolor_toracico_atipico = st.checkbox("Dolor Torácico Atípico")
    sindrome_coronario_agudo = st.checkbox("Síndrome Coronario Agudo")
    enfermedad_renal_cronica = st.checkbox("Enfermedad Renal Crónica")
    accidente_cerebrovascular_hemorragico = st.checkbox("Accidente Cerebrovascular Hemorrágico")
    taquicardia_supraventricular_paroxistica = st.checkbox("Taquicardia Supraventricular Paroxística")
    cardiopatia_congenita = st.checkbox("Cardiopatía Congénita")
    infeccion_tracto_urinario = st.checkbox("Infección del Tracto Urinario")
    sincopo_neurocardiogenico = st.checkbox("Síncope Neurocardiogénico")
    ortostatico = st.checkbox("Ortostático")
    endocarditis_infecciosa = st.checkbox("Endocarditis Infecciosa")
    shock = st.checkbox("Shock")

# Botón para hacer la predicción
if st.button('Realizar predicción'):
    # Corregimos los tipos
    # Transformar residencia, tipo_admision, genero en booleans
    residencia = 1 if residencia == "Urbana" else 0  
    tipo_admision = 0 if tipo_admision == "Emergencia" else 1  # "Emergencia"
    genero = 1 if genero == "Masculino" else 0  # Espacio innecesario removido

    # Transformar los checkboxes en 1 o en 0 los True y False
    # PROMPT: Transformar los checkboxes en 1 o en 0 (True o False)
    fumador = 1 if fumador else 0
    alcohol = 1 if alcohol else 0
    diabetes = 1 if diabetes else 0
    hipertension = 1 if hipertension else 0
    enfermedad_coronaria = 1 if enfermedad_coronaria else 0
    miocardiopatia = 1 if miocardiopatia else 0
    enfermedad_renal_cronica = 1 if enfermedad_renal_cronica else 0
    anemia_severa = 1 if anemia_severa else 0
    anemia = 1 if anemia else 0
    angina_estable = 1 if angina_estable else 0
    sindrome_coronario_agudo = 1 if sindrome_coronario_agudo else 0
    infarto_miocardio = 1 if infarto_miocardio else 0
    dolor_toracico_atipico = 1 if dolor_toracico_atipico else 0
    insuficiencia_card = 1 if insuficiencia_card else 0
    insuficiencia_eje_reducida = 1 if insuficiencia_eje_reducida else 0
    insuficiencia_eje_normal = 1 if insuficiencia_eje_normal else 0
    enfermedad_valvular = 1 if enfermedad_valvular else 0
    bloqueo_card = 1 if bloqueo_card else 0
    sindrome_nodo_sinusal = 1 if sindrome_nodo_sinusal else 0
    lesion_renal = 1 if lesion_renal else 0
    accidente_cerebrovascular_isquemico = 1 if accidente_cerebrovascular_isquemico else 0
    accidente_cerebrovascular_hemorragico = 1 if accidente_cerebrovascular_hemorragico else 0
    fibrilacion_auricular = 1 if fibrilacion_auricular else 0
    taquicardia_ventricular = 1 if taquicardia_ventricular else 0
    taquicardia_supraventricular_paroxistica = 1 if taquicardia_supraventricular_paroxistica else 0
    cardiopatia_congenita = 1 if cardiopatia_congenita else 0
    infeccion_tracto_urinario = 1 if infeccion_tracto_urinario else 0
    sincopo_neurocardiogenico = 1 if sincopo_neurocardiogenico else 0
    ortostatico = 1 if ortostatico else 0
    endocarditis_infecciosa = 1 if endocarditis_infecciosa else 0
    trombosis_venosa_profunda = 1 if trombosis_venosa_profunda else 0
    choque_cardiogenico = 1 if choque_cardiogenico else 0
    shock = 1 if shock else 0
    embolia_pulmonar = 1 if embolia_pulmonar else 0
    infeccion_toracica = 1 if infeccion_toracica else 0
    
    # Crear el vector de entrada para el modelo
    features = [
        edad, 
        genero, 
        residencia, 
        tipo_admision, 
        fumador, 
        alcohol, 
        diabetes, 
        hipertension, 
        enfermedad_coronaria, 
        miocardiopatia, 
        enfermedad_renal_cronica,  # 'Enfermedad Renal Crónica'
        anemia_severa, 
        anemia,  # Ahora se incluye la variable 'anemia'
        angina_estable, 
        sindrome_coronario_agudo,  # 'Síndrome Coronario Agudo'
        infarto_miocardio,  # 'Infarto de Miocardio(STEMI)'
        dolor_toracico_atipico, 
        insuficiencia_card, 
        insuficiencia_eje_reducida, 
        insuficiencia_eje_normal, 
        enfermedad_valvular, 
        bloqueo_card,
        sindrome_nodo_sinusal, 
        lesion_renal, 
        accidente_cerebrovascular_isquemico,  # 'Accidente Cerebrovascular Isquémico'
        accidente_cerebrovascular_hemorragico,  # 'Accidente Cerebrovascular Hemorrágico'
        fibrilacion_auricular, 
        taquicardia_ventricular, 
        taquicardia_supraventricular_paroxistica,  # 'Taquicardia Supraventricular Paroxística'
        cardiopatia_congenita,  # 'Cardiopatía Congénita'
        infeccion_tracto_urinario,  # 'Infección del Tracto Urinario'
        sincopo_neurocardiogenico,  # 'Síncope Neurocardiogénico'
        ortostatico,  # 'Ortostático'
        endocarditis_infecciosa,  # 'Endocarditis Infecciosa'
        trombosis_venosa_profunda,  # 'Trombosis Venosa Profunda'
        choque_cardiogenico, 
        shock, 
        embolia_pulmonar, 
        infeccion_toracica  # 'Infección Torácica'
    ]
    
    # Predicción con el modelo
    prediccion = model.predict([features])
    
    
    # Mostrar la predicción de "Motivo de Alta"
    if prediccion[0] == 0:
        motivo = "Motivo de Alta: Alta contra el juicio del facultativo"
    elif prediccion[0] == 1:
        motivo = "Motivo de Alta: Salud Plena"
    else:
        motivo = "Motivo de Alta: Fallecido"

    st.markdown(f"<p class='stText'>{motivo}</p>", unsafe_allow_html=True)

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
            0: "Alta contra el juicio del facultativo",
            1: "Alta Médica",
            2: "Fallecimiento"
        })

        # Mostrar las predicciones junto con los datos originales
        st.subheader("Predicciones:")
        st.write(df_original)

        # Convertir a CSV
        csv = df_original.to_csv(index=False).encode("utf-8")

        # Convertir a XLSX
        def convertir_a_xlsx(df):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Predicciones')
            processed_data = output.getvalue()
            return processed_data

        xlsx = convertir_a_xlsx(df_original)


        # Crear botones de descarga
        st.download_button("Descargar CSV", csv, file_name="predicciones.csv", mime="text/csv")
        st.download_button("Descargar XLSX", xlsx, file_name="predicciones.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        
    # Resumen estadístico de la columna "Predicción"

    if 'Predicción' in df_original.columns:
        st.subheader("Resumen estadístico de las predicciones:")

        # Muestra la cantidad de cada tipo de predicción con porcentajes
        pred_counts = df_original['Predicción'].value_counts()
        pred_percentage = (pred_counts / pred_counts.sum()) * 100
        pred_summary = pd.DataFrame({
            'Predicción': pred_counts.index,
            'Cantidad': pred_counts.values,
            'Porcentaje': pred_percentage.values
        })

        # Mostrar el resumen con porcentajes
        st.write(pred_summary)

        # Gráfico de barras usando Altair
        st.subheader("Distribución de las predicciones:")

        chart = alt.Chart(pred_summary).mark_bar().encode(
            x=alt.X('Predicción:N', title='Motivo de Alta'),
            y=alt.Y('Cantidad:Q', title='Número de Predicciones'),
            color='Predicción:N',
            tooltip=['Predicción', 'Cantidad', 'Porcentaje']
        ).properties(
            title="Distribución de las Predicciones"
        ).configure_mark(
            opacity=0.8,
            color='darkblue'
        )

        # Mostrar gráfico
        st.altair_chart(chart, use_container_width=True)