import pandas as pd

# 1. Cargar el dataset
archivo = "gender_submission.csv"
df = pd.read_csv(archivo)

# 2. Resumen general
print("========================================")
print("     ANÁLISIS DE DATOS - TITANIC        ")
print("========================================")
print(f"Total de registros: {len(df)}")
print(f"Columnas detectadas: {list(df.columns)}\n")

# 3. Mostrar las primeras 5 filas
print("--- Primeras 5 filas ---")
print(df.head())
print()

# 4. Análisis de Calidad de Datos
print("--- Análisis de Calidad ---")
print("Valores nulos por columna:")
print(df.isnull().sum())

print(f"\nFilas duplicadas: {df.duplicated().sum()}")

# 5. Distribución de la variable 'Survived'
print("\n--- Distribución de Supervivencia ---")
conteo = df["Survived"].value_counts()
porcentaje = df["Survived"].value_counts(normalize=True) * 100

print(f"Fallecidos (0): {conteo.get(0, 0)} ({porcentaje.get(0, 0):.2f}%)")
print(f"Supervivientes (1): {conteo.get(1, 0)} ({porcentaje.get(1, 0):.2f}%)")