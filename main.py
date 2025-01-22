import pandas as pd

df = pd.read_excel("./Data/Dataset.xls")

df['Descripción'] = df['Descripción'].fillna('No description')
df['Servicio'] = df['Servicio'].fillna('Unspecified')
df['Torre'] = df['Torre'].fillna('Unspecified')
df['Entorno'] = df['Entorno'].fillna('Unspecified')
df['Estado cumplimiento SLA'] = df['Estado cumplimiento SLA'].fillna('Unspecified')

df.to_excel('./Data/New_Dataset.xlsx', index=False)

df = pd.read_excel("./Data/New_Dataset.xlsx")

print(df.info())
