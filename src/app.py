import streamlit as st
from pickle import load

# Cargar el modelo
model = load(open("/workspaces/c23-14-data/Models/Model_RF.sav", "rb"))

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
    angina_estable = st.checkbox("Angina Estable")
    infarto_miocardio = st.checkbox("Infarto de Miocardio (STEMI)")
    dolor_toracico_atipico = st.checkbox("Dolor Torácico Atípico")

# Botón para hacer la predicción
if st.button('Realizar predicción'):
    # Corregimos los tipos
    # Transformar residencia, tipo_admision, genero en booleans
    residencia = 1 if residencia == "Urbana" else 0  
    tipo_admision = 1 if tipo_admision == "Emergencia" else 0  # "Emergencia"
    genero = 1 if genero == "Masculino" else 0  # Espacio innecesario removido

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
        enfermedad_renal,  # Corrección: 'Enfermedad Renal Crónica'
        anemia_severa, 
        anemia, 
        angina_estable, 
        sindrome_coronario_agudo,  # Corrección: 'Síndrome Coronario Agudo'
        infarto_miocardio,  # Corrección: 'Infarto de Miocardio(STEMI)'
        dolor_toracico_atipico, 
        insuficiencia_card, 
        insuficiencia_eje_reducida, 
        insuficiencia_eje_normal, 
        enfermedad_valvular, 
        bloqueo_card,
        sindrome_nodo_sinusal, 
        lesion_renal, 
        accidente_cerebrovascular_isquemico,  # Corrección: 'Accidente Cerebrovascular Isquémico'
        accidente_cerebrovascular_hemorragico,  # Corrección: 'Accidente Cerebrovascular Hemorrágico'
        fibrilacion_auricular, 
        taquicardia_ventricular, 
        taquicardia_supraventricular_paroxistica,  # Corrección: 'Taquicardia Supraventricular Paroxística'
        cardiopatia_congenita,  # Corrección: 'Cardiopatía Congénita'
        infeccion_tracto_urinario,  # Corrección: 'Infección del Tracto Urinario'
        sincopo_neurocardiogenico,  # Corrección: 'Síncope Neurocardiogénico'
        ortostatico,  # Corrección: 'Ortostático'
        endocarditis_infecciosa,  # Corrección: 'Endocarditis Infecciosa'
        trombosis_venosa_profunda,  # Corrección: 'Trombosis Venosa Profunda'
        choque_cardiogenico, 
        shock, 
        embolia_pulmonar, 
        infeccion_toracica  # Corrección: 'Infección Torácica'
    ]
    
    # Predicción con el modelo
    prediccion = model.predict([features])
    
    # Mostrar la predicción de "Motivo de Alta"
    if prediccion[0] == 0:
        motivo = "Motivo de Alta: Alta contra el juicio del facultativo"
    elif prediccion[0] == 1:
        motivo = "Motivo de Alta: Salud plena"
    else:
        motivo = "Motivo de Alta: Fallecimiento"

    st.markdown(f"<p class='stText'>{motivo}</p>", unsafe_allow_html=True)

    # Listo
    
