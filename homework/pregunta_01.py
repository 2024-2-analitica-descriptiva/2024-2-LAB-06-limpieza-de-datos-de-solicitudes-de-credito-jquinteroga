"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd 
import os 

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    """
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

    file_path = 'files/input/solicitudes_de_credito.csv' 
    data = pd.read_csv(file_path, sep=';') 

    # Limpieza del DataFrame
    data.drop(['Unnamed: 0'], axis=1, inplace=True) 
    data.dropna(inplace=True) 
    data.drop_duplicates(inplace=True) 

    # columna 'fecha_de_beneficio'
    data[['día', 'mes', 'año']] = data['fecha_de_beneficio'].str.split('/', expand=True) 
    data.loc[data['año'].str.len() < 4, ['día', 'año']] = data.loc[data['año'].str.len() < 4, ['año', 'día']].values  
    data['fecha_de_beneficio'] = data['año'] + '-' + data['mes'] + '-' + data['día'] 
    data.drop(['día', 'mes', 'año'], axis=1, inplace=True) 

    # columnas de texto
    object_columns = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito'] 
    data[object_columns] = data[object_columns].apply(lambda x: x.str.lower().replace(['-', '_'], ' ', regex=True).str.strip()) 
    data['barrio'] = data['barrio'].str.lower().replace(['-', '_'], ' ', regex=True) 

    # columna 'monto_del_credito'
    data['monto_del_credito'] = data['monto_del_credito'].str.replace("[$, ]", "", regex=True).str.strip() 
    data['monto_del_credito'] = pd.to_numeric(data['monto_del_credito'], errors='coerce') 
    data['monto_del_credito'] = data['monto_del_credito'].fillna(0).astype(int) 
    data['monto_del_credito'] = data['monto_del_credito'].astype(str).str.replace('.00', '') 

     # Elimina duplicados 
    data.drop_duplicates(inplace=True)

    output_dir = 'files/output' # Define la carpeta de salida
    os.makedirs(output_dir, exist_ok=True)

    output_path = f'{output_dir}/solicitudes_de_credito.csv'
    data.to_csv(output_path, sep=';', index=False) # Guarda el DataFrame como CSV.

    return data.head()

df_limpio = pregunta_01()
print(df_limpio.head())
