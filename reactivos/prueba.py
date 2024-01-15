import pandas as pd
import re


# Suponiendo que el archivo de texto tiene líneas separadas por saltos de línea
with open(r'H:\Django\ProyectoDjango_p\Proyecto1_p\reactivos' + '\\' + 'Reactivos 413N_5.txt', 'r', encoding='utf-8', errors='ignore') as f:
    # Lee las líneas del archivo
    lines = f.readlines()

# Suponiendo que las columnas están separadas por comas (puedes ajustar esto según tu formato)
data = [line.strip().split('\t') for line in lines]

# Suponiendo que la primera línea contiene los nombres de las columnas
columns = data[0]

# Crear el DataFrame

df = pd.DataFrame(data[1:])
df2=pd.DataFrame({
        'identificacion': df[1],
        'nombre':df[3],
        'name':df[2], 
        'marca':df[4],
        'cas': df[5],
        'categoria':df[6],
        'sedronar': df[7],
        'abierto':df[8],
        'cantidad_numero':df[9], 
        'unidad':df[10]})

print(df2['categoria'][1])
for i in range(len(df2)):
    print(f"rvo{i+3}=Producto(categorias=categoria_{df2['categoria'][i]}, nombre='{df2['nombre'][i]}', name='{df2['name'][i]}', cantidad={df2['cantidad_numero'][i]}, unidad='{df2['unidad'][i]}', marca='{df2['marca'][i]}', CAS= '{df2['cas'][i]}', sedronar={df2['sedronar'][i]}, abierto={df2['abierto'][i]}, numero=1, identificacion= '{df2['identificacion'][i]}')")
    
# Ahora puedes acceder a las columnas por nombre


#(df.iloc[:, 2]).to_csv(r'H:\Django\ProyectoDjango_p\Proyecto1_p\reactivos' + '\\' + 'fila_413N_2.csv')

# Iterar sobre las filas y generar instancias de Producto
'''for i, row in df.iterrows():
    producto_instance = df2(
        categorias=row['categoria'],
        nombre=row['nombre'],
        name=row['name'],
        cantidad=row['cantidad_numeros'],
        unidad=row['unidad'],
        marca=row['marca'],
        CAS=row['CAS'],
        sedronar=row['sedronar'],
        abierto=row['abierto'],
    )

    # Imprimir la instancia o realizar cualquier acción que desees
    print(f'rvo{i+1}={producto_instance}')

for i, row in df2.iterrows():
    producto_instance = Producto(
        identificacion=row['identificacion'],
        categorias=row['categoria'],  # Asegúrate de que el nombre de la columna sea correcto
        nombre=row['nombre'],
        name=row['name'],
        cantidad=row['cantidad_numeros'],
        unidad=row['unidad'],
        marca=row['marca'],
        CAS=row['cas'],
        sedronar=row['sedronar'],
        abierto=row['abierto'],
    )
    producto_instance.save() '''
