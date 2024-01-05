## escriba el pipeline aqui

import pandas as pd
from sqlalchemy import create_engine


# Ruta del archivo
archivo_csv = '../data/data.csv'

# Create your views here.
def function():
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(archivo_csv, header=0,delimiter=',')

    #  Nombrar columnas
    df.columns = ['fecha','tipo_de_cambio']

    
    # Ruta al archivo de la base de datos SQLite
    path = 'sqlite:///C:/Users/Love/Desktop/all/Newapi/anoctua.sqlite'

    # Conexion a la base de datos SQLite
    engine = create_engine(path)

    # Cargar datos en la tabla "cotizaciones"
    df.to_sql('cotizaciones', engine, if_exists='append', index=False)

    # Consultar los datos recién insertados
    new_data = pd.read_sql('SELECT * FROM cotizaciones', engine)

    print(new_data)
    # Mensaje de confirmacion
    print("Datos cargados exitosamente en la tabla.")



if __name__ == "__main__":
    function()