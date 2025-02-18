import pandas as pd

# Criando o DataFrame
data = {
    'Data': ['15/01/2025', '15/01/2025', '15/01/2025', '15/01/2025', '15/01/2025'],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Porto Alegre', 'Salvador'],
    'Temperatura Máxima (°C)': [30.5, 35.0, 24.0, 28.0, 31.0],
    'Temperatura Mínima (°C)': [22.0, 25.0, 18.0, 20.0, 24.5],
    'Precipitação (mm)': [12.0, None, 8.0, 15.0, None],
    'Umidade Relativa (%)': [78, 70, None, 82, 80]
}

df = pd.DataFrame(data)

print(df)

print("\nVerificando valores ausentes:")
print(df.isnull())
print("\nQuantidade de valores ausentes por coluna:")
print(df.isnull().sum())



# Removendo linhas com valores ausentes
df_cleaned = df.dropna()
print("\nDados após remover linhas com valores ausentes:")
print(df_cleaned)



# Substituindo valores ausentes na coluna Precipitação pela média da Precipitação
df['Precipitação (mm)'] = df['Precipitação (mm)'].fillna(df['Precipitação (mm)'].mean())

# Substituindo valores ausentes na coluna Umidade Relativa pela mediana da Umidade Relativa
df['Umidade Relativa (%)'] = df['Umidade Relativa (%)'].fillna(df['Umidade Relativa (%)'].median())

print("\nDados após preencher valores ausentes em 'Precipitação' e 'Umidade Relativa':")
print(df)

 

# Adicionando uma nova coluna chamada Amplitude Térmica
df['Amplitude Térmica'] = df['Temperatura Máxima (°C)'] - df['Temperatura Mínima (°C)']

print(df)

 



# Reordenando o DataFrame para que as colunas fiquem na seguinte ordem:
df = df[['Data', 'Cidade', 'Temperatura Máxima (°C)', 'Temperatura Mínima (°C)', 'Amplitude Térmica', 'Precipitação (mm)', 'Umidade Relativa (%)']]

# Exibindo o DataFrame modificado
print("DataFrame reordenado:")
print(df)



# Criando um novo DataFrame contendo apenas as cidades com Temperatura Máxima acima de 30°C
df_high_temp = df[df['Temperatura Máxima (°C)'] > 30]

print("\nDataFrame com cidades com Temperatura Máxima acima de 30°C:\n")
print(df_high_temp)









                
