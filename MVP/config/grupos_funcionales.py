# Grupos Funcionales
# config/grupos_funcionales.py
"""Módulo: grupos_funcionales - Define la organización de las características en la interfaz."""

grupos_funcionales = {
    "Datos Demográficos": ['Edad', 'Género', 'Residencia'],
    "Tipo de Admisión": ['Tipo de Admisión'],
    "Hábitos y Factores de Riesgo": [
        'Fumador', 'Alcohol', 'Diabetes Mellitus', 
        'Hipertensión', 'Enfermedad Coronaria Arterial'
    ],
    "Enfermedades Cardíacas": [
        'Miocardiopatía', 'Insuficiencia Cardíaca',
        'Insuficiencia Cardíaca con Fracción de Eyección Reducida',
        'Insuficiencia Cardíaca con Fracción de Eyección Normal',
        'Enfermedad Valvular Cardíaca', 'Bloqueo Cardíaco Completo'
    ],
    "Complicaciones Agudas": [
        'Síndrome del Nodo Sinusal Enfermo', 'Lesión Renal Aguda',
        'Accidente Cerebrovascular Isquémico', 'Accidente Cerebrovascular Hemorrágico',
        'Fibrilación Auricular', 'Taquicardia Ventricular',
        'Taquicardia Supraventricular Paroxística', 'Choque Cardiogénico', 'Shock'
    ],
    "Infecciones y Trombosis": [
        'Embolia Pulmonar', 'Infección Torácica',
        'Trombosis Venosa Profunda', 'Endocarditis Infecciosa'
    ],
    "Otras Condiciones": [
        'Anemia Severa', 'Anemia', 'Angina Estable',
        'Síndrome Coronario Agudo', 'Infarto de Miocardio(STEMI)',
        'Dolor Torácico Atípico', 'Cardiopatía Congénita',
        'Infección del Tracto Urinario', 'Síncope Neurocardiogénico', 'Ortostático'
    ]
}