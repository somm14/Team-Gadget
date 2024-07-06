import pandas as pd
import sqlite3

def bienvenida():
    print('''Bienvenido detective a esta investigación.\n
          Ha ocurrido un crimen y el detective necesita tu ayuda.\n 
          El detective te dio el informe de la escena del crimen, pero de alguna manera lo perdiste.\n
          Recuerdas vagamente que el crimen fue un ​asesinato​ que ocurrió en algún momento del ​15 de enero de 2018​ y que tuvo lugar en ​SQL City​.\n 
          Comience recuperando el informe de la escena del crimen correspondiente de la base de datos del departamento de policía.''')

def pistas_1():
    print('''Pistas:\n
          - Crimen: asesinato
          - Fecha: 15 de enero del 2018
          - Lugar: SQL City
''')
    
# Conectamos con la base de datos chinook.db
conn = sqlite3.connect("./data/sql-murder-mystery.db")

# Obtenemos un cursor que utilizaremos para hacer las queries
cursor = conn.cursor()

# Query para ver el informe del crimen

query = '''
SELECT *
FROM crime_scene_report
WHERE ("date" LIKE 20180115) AND (type = "murder") AND (city LIKE "SQL City");
'''
def informe():
    informe = pd.read_sql(query, conn)
    print("Imforme del crimen:")
    for lineas in informe["description"]:
        print(lineas)

def pistas_2():
    print('''\nSiguientes pistas:\n
          - Primer testigo: Vive en la última casa de Northwestern Dr
          - Segundo testigo: Se llama Annabel y viven en algún lugar de Franklin Ave
''')
# Query para saber quién es la testigo_1


# Al estar ubicada en la última casa realizamos lo siguiente



