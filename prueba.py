import pandas as pd
import mysql.connector
import re

# conexion = mysql.connector.connect(
#         host="172.16.0.50",
#         port=3306,
#         user="interclinica_dev",
#         password="SecureDb@2025",
#         database="db_registros_medicos"
# )

# Datos que simulan ser extraídos de tbl_pacientes

data_pacientes = {
    'id_interno': ['PCNT001', 'PCNT002', 'PCNT003', 'PCNT004'],
    'rut_paciente': ['11111111-1', '22.222.222-2', '33333333-3', '44.444.444k'],
    'nombre_paciente': ['Ana Soto', 'Carlos Ríos', 'Elena Vera', 'Francisco Paz'],
    'fecha_nacimiento': ['1985-03-10', '1990-07-22', '1978-11-05', '2000-01-01']
}
df_pacientes_raw = pd.DataFrame(data_pacientes)

# Datos que simulan ser extraídos de tbl_exámenes_solicitados

data_examenes_solicitados = {
    'id_solicitud': [1001, 1002, 1003, 1004, 1005],
    'id_interno': ['PCNT001', 'PCNT002', 'PCNT001', 'PCNT003', 'PCNT004'],
    'tipo_examen': ['Hemograma', 'Perfil Lipídico', 'Radiografía Tórax', 'Glicemia', 'Orina Completa'],
    'fecha_solicitud': ['2024-01-15 09:00:00', '2024-01-16 10:15:00', '2024-01-15 11:30:00', '2024-01-17 08:45:00', '2024-01-18 14:00:00'],
    'estado_solicitud': ['Realizado', 'Pendiente', 'Realizado', 'Realizado', 'Pendiente']
}
df_examenes_solicitados_raw = pd.DataFrame(data_examenes_solicitados)

# Datos que simulan ser extraídos de tbl_resultados_exámenes

data_resultados_examenes = {
    'codigo_solicitud': [' 1001 ', '1002', ' 1003 ', '1004', '1005'],
    'valor_resultado': ['5.2', '15,3', '120.5 mg/dL', '95.0', '6,5l'],
    'unidad_medida': ['millones/uL', 'mg/dL', 'mg/dL', 'mg/dL', 'mg/dL'],
    'observaciones': ['Normal', 'Pendiente de resultado', 'Sin hallazgos', 'Dentro de rango', 'Sin observaciones']
}
df_resultados_examenes_raw = pd.DataFrame(data_resultados_examenes)

# Agrego los puntos y guion a los RUTs

def rut_p(rut_raw):
    rut = rut_raw.replace(".", "").replace("-", "").upper()
    cuerpo = rut[:-1]
    dv = rut[-1]
    cuerpo_formateado = f"{int(cuerpo):,}".replace(",", ".")
    return f"{cuerpo_formateado}-{dv}"

df_pacientes_raw['rut_paciente'] = df_pacientes_raw['rut_paciente'].apply(rut_p)

# Cambiar a fecha y hora
df_pacientes_raw['fecha_nacimiento'] = pd.to_datetime(df_pacientes_raw['fecha_nacimiento'])
df_examenes_solicitados_raw['fecha_solicitud'] = pd.to_datetime(df_examenes_solicitados_raw['fecha_solicitud'])

# Limpiar espacios y convertir codigo_solicitud a int
df_resultados_examenes_raw['codigo_solicitud'] = df_resultados_examenes_raw['codigo_solicitud'].str.strip()
df_resultados_examenes_raw['codigo_solicitud'] = df_resultados_examenes_raw['codigo_solicitud'].astype(int)

# Limpiamos texto y convertimos a valor numérico
def limpiar_valor(valor):
    valor = valor.replace(',', '.').lower()  # reemplaza coma por punto, y pasa a minúsculas
    numeros = re.findall(r"\d+\.?\d*", valor)
    return float(numeros[0]) if numeros else None

# Unir exámenes con pacientes
df_combinado = pd.merge(df_examenes_solicitados_raw, df_pacientes_raw, on='id_interno', how='left')

# Unir con resultados
df_completo = pd.merge(df_combinado, df_resultados_examenes_raw,
                    left_on='id_solicitud', right_on='codigo_solicitud', how='left')

# Seleccionar y reordenar columnas finales
df_final = df_completo[[
    'id_solicitud', 'id_interno', 'nombre_paciente', 'rut_paciente', 'fecha_nacimiento',
    'tipo_examen', 'fecha_solicitud', 'estado_solicitud',
    'valor_resultado', 'unidad_medida', 'observaciones'
]]

# VALIDACIÓN

# Primeras 5 filas
print("\nPrimeras 5 filas con columnas seleccionadas:\n")
print(df_final[['id_solicitud', 'id_interno', 'nombre_paciente', 'rut_paciente', 'fecha_nacimiento']].head())

# Tipos de datos
print("\nTipos de datos de cada columna:\n")
print(df_final.dtypes)

# Cantidad de valores nulos en valor_resultado
print("\nCantidad de valores nulos en 'valor_resultado':")
print(df_final['valor_resultado'].isnull().sum())