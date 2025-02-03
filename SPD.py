import pandas as pd

path1 = 'caminho do primeiro arquivo'
path2 = 'caminho do segundo arquivo'

df_info = pd.read_csv(path1)

df_vendas = pd.read_csv(path2)

df_merged = df_vendas.merge(df_info, on='ID')

df_merged['Tempo'] = df_merged['Data'].dt.to_period('M')

df_merged['Total'] = df_merged['Valor'] * df_merged['Quantidade']

df_final = df_merged.groupby(['ID', 'Tempo'])['Total'].sum().reset_index()

df_final
