# se ejecuta con streamlit run src/app.py
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
    tipo_admision = 1 if tipo_admision == "Emergencia" else 0  # "Emergencia"
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
        motivo = "Motivo de Alta: Salud plena"
    else:
        motivo = "Motivo de Alta: Fallecido"

    st.markdown(f"<p class='stText'>{motivo}</p>", unsafe_allow_html=True)

     # Mostrar las features y sus valores
    st.subheader("Valores de las características:")
    for feature, value in zip([
        "Edad", "Género", "Residencia", "Tipo de Admisión", "Fumador", "Consumo de Alcohol", 
        "Diabetes Mellitus", "Hipertensión", "Enfermedad Coronaria", "Miocardiopatía", 
        "Enfermedad Renal Crónica", "Anemia Severa", "Anemia", "Angina Estable", 
        "Síndrome Coronario Agudo", "Infarto de Miocardio (STEMI)", "Dolor Torácico Atípico", 
        "Insuficiencia Cardíaca", "Insuficiencia Cardíaca con Fracción de Eyección Reducida", 
        "Insuficiencia Cardíaca con Fracción de Eyección Normal", "Enfermedad Valvular Cardíaca", 
        "Bloqueo Cardíaco Completo", "Síndrome del Nodo Sinusal Enfermo", "Lesión Renal Aguda", 
        "Accidente Cerebrovascular Isquémico", "Accidente Cerebrovascular Hemorrágico", 
        "Fibrilación Auricular", "Taq. Ventricular", "Taquicardia Supraventricular Paroxística", 
        "Cardiopatía Congénita", "Infección del Tracto Urinario", "Síncope Neurocardiogénico", 
        "Ortostático", "Endocarditis Infecciosa", "Trombosis Venosa Profunda", "Choque Cardiogénico", 
        "Shock", "Embolia Pulmonar", "Infección Torácica"
    ], features):
        st.write(f"{feature}: {value}")