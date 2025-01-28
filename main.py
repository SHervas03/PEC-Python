import pandas as pd

def aaa(df_default):
    df_default['Descripción'] = df_default['Descripción'].fillna('No description')
    df_default['Servicio'] = df_default['Servicio'].fillna('Unspecified')
    df_default['Torre'] = df_default['Torre'].fillna('Unspecified')
    df_default['Entorno'] = df_default['Entorno'].fillna('Unspecified')
    df_default['Estado cumplimiento SLA'] = df_default['Estado cumplimiento SLA'].fillna('Unspecified')
    return df_default

def bbb(df, df_new_path):
    df.to_excel(df_new_path, index=False)


def ccc(df):
    print(df.info())



if __name__ == "__main__":
    df_default = "./Data/Dataset.xls"
    df_new =  './Data/New_Dataset.xlsx'
    df_dflt = pd.read_excel(df_default)

    ccc(df_dflt)
    df = aaa(df_dflt)
    ccc(df)
    bbb(df, df_new)
    df_nw = pd.read_excel(df_new)
    ccc(df_nw)



