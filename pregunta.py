"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.set_index(df.columns[0], inplace= True)

    df= df.copy()

    df["sexo"] = df["sexo"].str.lower()

    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()

    df["idea_negocio"] = df["idea_negocio"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.replace("_"," ")
    df["idea_negocio"] = df["idea_negocio"].str.replace("-"," ")
    df["idea_negocio"] = df["idea_negocio"].str.strip()

    df["barrio"] = df["barrio"].str.lower()
    df["barrio"] = df["barrio"].str.replace("_"," ")
    df["barrio"] = df["barrio"].str.replace("-"," ")

    df["comuna_ciudadano"] = df["comuna_ciudadano"].replace(".",",")

    df["fecha_de_beneficio_1"] = pd.to_datetime(df.fecha_de_beneficio, format = "%Y/%m/%d", errors ="coerce")
    df["fecha_de_beneficio_2"] = pd.to_datetime(df.fecha_de_beneficio, format = "%d/%m/%Y", errors ="coerce")
    df["fecha_de_beneficio"] = df.apply(lambda x: f"{x['fecha_de_beneficio_1']} {x['fecha_de_beneficio_2']}", axis = 1)
    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].str.replace("NaT ","")
    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].str.replace(" NaT","")
    df["fecha_de_beneficio"]= pd.to_datetime(df["fecha_de_beneficio"])


    df["monto_del_credito"] = df["monto_del_credito"].str.replace("$ ","")
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(",","")
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(".00","")
    df["monto_del_credito"] = df["monto_del_credito"].str.strip()

    df["línea_credito"] = df["línea_credito"].str.lower()
    df["línea_credito"] = df["línea_credito"].str.replace("_"," ")
    df["línea_credito"] = df["línea_credito"].str.replace("-"," ")
    df["línea_credito"] = df["línea_credito"].str.strip()


    df= df.drop(["fecha_de_beneficio_1", "fecha_de_beneficio_2"], axis = 1)

    df = df.dropna(subset=["tipo_de_emprendimiento", "barrio"], how = "any")
    df = df.drop_duplicates()

    df= df.sort_values(by = ["sexo", "tipo_de_emprendimiento", "idea_negocio", "barrio", "estrato", "comuna_ciudadano", "fecha_de_beneficio", "monto_del_credito", "línea_credito"], ascending=[False, False, False, False, False, False, False, False, False])

    df.to_csv("df_prueba_aj_def.csv")

    
    return df