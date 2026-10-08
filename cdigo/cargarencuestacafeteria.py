import pandas as pd

# 1. Levantar el archivo CSV
encuesta = pd.read_csv(
    "encuestacafeteria.csv",
    sep=None,
    engine="python",
    encoding="latin1"
)

# Limpiar posibles espacios en los nombres de columnas
encuesta.columns = encuesta.columns.str.strip()

# 2. Declarar/modificar los tipos según el libro de códigos

# ID: entero
encuesta["id"] = pd.to_numeric(
    encuesta["id"],
    errors="coerce"
).astype("Int64")

# Frecuencia: ordinal
encuesta["frecuencia"] = pd.Categorical(
    encuesta["frecuencia"],
    categories=[
        "Nunca",
        "1 a 3 veces",
        "4 a 8 veces",
        "Más de 8 veces"
    ],
    ordered=True
)

# Productos: variables binarias
encuesta["prod_cafe"] = pd.to_numeric(
    encuesta["prod_cafe"], errors="coerce"
).astype("Int64")

encuesta["prod_comida"] = pd.to_numeric(
    encuesta["prod_comida"], errors="coerce"
).astype("Int64")

encuesta["prod_frias"] = pd.to_numeric(
    encuesta["prod_frias"], errors="coerce"
).astype("Int64")

encuesta["prod_otros"] = pd.to_numeric(
    encuesta["prod_otros"], errors="coerce"
).astype("Int64")

# Atención: ordinal de 1 a 5
encuesta["atencion"] = pd.to_numeric(
    encuesta["atencion"], errors="coerce"
)

encuesta["atencion"] = pd.Categorical(
    encuesta["atencion"],
    categories=[1, 2, 3, 4, 5],
    ordered=True
)

# Medios de pago: variables binarias
encuesta["pago_efectivo"] = pd.to_numeric(
    encuesta["pago_efectivo"], errors="coerce"
).astype("Int64")

encuesta["pago_tarjeta"] = pd.to_numeric(
    encuesta["pago_tarjeta"], errors="coerce"
).astype("Int64")

encuesta["pago_transferencia"] = pd.to_numeric(
    encuesta["pago_transferencia"], errors="coerce"
).astype("Int64")

# Estudiante: variable booleana TRUE/FALSE
encuesta["estudiante"] = encuesta["estudiante"].replace({
    "TRUE": True,
    "FALSE": False,
    "True": True,
    "False": False
}).astype("boolean")

# Edad: cuantitativa
encuesta["edad"] = pd.to_numeric(
    encuesta["edad"], errors="coerce"
).astype("Int64")

# Mejora: texto
encuesta["mejora"] = encuesta["mejora"].astype("string")

# 3. Mostrar la tabla
print(encuesta)

# 4. Mostrar los tipos finales
print("\nTIPOS DE VARIABLES:")
print(encuesta.dtypes)