# Utilizando a biblioteca Pandas para criar e modificar um DataFrame

````python
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
````
## DataFrame Original:

| Data       | Cidade         | Temperatura Máxima (°C) | Temperatura Mínima (°C) | Precipitação (mm) | Umidade Relativa (%) |
|------------|---------------|-------------------------|-------------------------|-------------------|----------------------|
| 15/01/2025 | São Paulo     | 30.5                    | 22.0                    | 12.0              | 78.0                 |
| 15/01/2025 | Rio de Janeiro | 35.0                   | 25.0                    | NaN               | 70.0                 |
| 15/01/2025 | Curitiba      | 24.0                    | 18.0                    | 8.0               | NaN                  |
| 15/01/2025 | Porto Alegre  | 28.0                    | 20.0                    | 15.0              | 82.0                 |
| 15/01/2025 | Salvador      | 31.0                    | 24.5                    | NaN               | 80.0                 |

````py
print("\nVerificando valores ausentes:")
print(df.isnull())
print("\nQuantidade de valores ausentes por coluna:")
print(df.isnull().sum())
````
## Verificando valores ausentes:

|   | Data  | Cidade | Temperatura Máxima (°C) | Temperatura Mínima (°C) | Precipitação (mm) | Umidade Relativa (%) |
|---|------|--------|-------------------------|-------------------------|-------------------|----------------------|
| 0 | False | False  | False                   | False                   | False             | False               |
| 1 | False | False  | False                   | False                   | True              | False               |
| 2 | False | False  | False                   | False                   | False             | True                |
| 3 | False | False  | False                   | False                   | False             | False               |
| 4 | False | False  | False                   | False                   | True              | False               |

---

## Quantidade de valores ausentes por coluna:

| Coluna                      | Valores Ausentes |
|-----------------------------|-----------------|
| Data                        | 0               |
| Cidade                      | 0               |
| Temperatura Máxima (°C)     | 0               |
| Temperatura Mínima (°C)     | 0               |
| Precipitação (mm)           | 2               |
| Umidade Relativa (%)        | 1               |

````py
# Removendo linhas com valores ausentes
df_cleaned = df.dropna()
print("\nDados após remover linhas com valores ausentes:")
print(df_cleaned)
````

## Dados após remover linhas com valores ausentes:

| Data       | Cidade         | Temperatura Máxima (°C) | Temperatura Mínima (°C) | Precipitação (mm) | Umidade Relativa (%) |
|------------|---------------|-------------------------|-------------------------|-------------------|----------------------|
| 15/01/2025 | São Paulo     | 30.5                    | 22.0                    | 12.000000         | 78.0                 |
| 15/01/2025 | Rio de Janeiro | 35.0                   | 25.0                    | 11.666667         | 70.0                 |
| 15/01/2025 | Porto Alegre  | 28.0                    | 20.0                    | 15.000000         | 82.0                 |
| 15/01/2025 | Salvador      | 31.0                    | 24.5                    | 11.666667         | 80.0                 |


````py
# Substituindo valores ausentes na coluna Precipitação pela média da Precipitação
df['Precipitação (mm)'] = df['Precipitação (mm)'].fillna(df['Precipitação (mm)'].mean())

# Substituindo valores ausentes na coluna Umidade Relativa pela mediana da Umidade Relativa
df['Umidade Relativa (%)'] = df['Umidade Relativa (%)'].fillna(df['Umidade Relativa (%)'].median())

print("\nDados após preencher valores ausentes em 'Precipitação' e 'Umidade Relativa':")
print(df)
````

## Dados após preencher valores ausentes em 'Precipitação' e 'Umidade Relativa':

| Data       | Cidade         | Temperatura Máxima (°C) | Temperatura Mínima (°C) | Precipitação (mm) | Umidade Relativa (%) |
|------------|---------------|-------------------------|-------------------------|-------------------|----------------------|
| 15/01/2025 | São Paulo     | 30.5                    | 22.0                    | 12.000000         | 78.0                 |
| 15/01/2025 | Rio de Janeiro | 35.0                   | 25.0                    | 11.666667         | 70.0                 |
| 15/01/2025 | Curitiba      | 24.0                    | 18.0                    | 8.000000          | 79.0                 |
| 15/01/2025 | Porto Alegre  | 28.0                    | 20.0                    | 15.000000         | 82.0                 |
| 15/01/2025 | Salvador      | 31.0                    | 24.5                    | 11.666667         | 80.0                 |


````py
# Adicionando uma nova coluna chamada Amplitude Térmica
df['Amplitude Térmica'] = df['Temperatura Máxima (°C)'] - df['Temperatura Mínima (°C)']

print(df)
````

## Dados com Amplitude Térmica:

| Data       | Cidade         | Temperatura Máxima (°C) | Temperatura Mínima (°C) | Precipitação (mm) | Umidade Relativa (%) | Amplitude Térmica |
|------------|---------------|-------------------------|-------------------------|-------------------|----------------------|-------------------|
| 15/01/2025 | São Paulo     | 30.5                    | 22.0                    | 12.000000         | 78.0                 | 8.5               |
| 15/01/2025 | Rio de Janeiro | 35.0                   | 25.0                    | 11.666667         | 70.0                 | 10.0              |
| 15/01/2025 | Curitiba      | 24.0                    | 18.0                    | 8.000000          | 79.0                 | 6.0               |
| 15/01/2025 | Porto Alegre  | 28.0                    | 20.0                    | 15.000000         | 82.0                 | 8.0               |
| 15/01/2025 | Salvador      | 31.0                    | 24.5                    | 11.666667         | 80.0                 | 6.5               |

````py
# Reordenando o DataFrame para que as colunas fiquem na seguinte ordem:
df = df[['Data', 'Cidade', 'Temperatura Máxima (°C)', 'Temperatura Mínima (°C)', 'Amplitude Térmica', 'Precipitação (mm)', 'Umidade Relativa (%)']]

# Exibindo o DataFrame modificado
print("DataFrame reordenado:")
print(df)
````

## DataFrame Reordenado:

| Data       | Cidade         | Temperatura Máxima (°C) | Temperatura Mínima (°C) | Amplitude Térmica | Precipitação (mm) | Umidade Relativa (%) |
|------------|---------------|-------------------------|-------------------------|-------------------|-------------------|----------------------|
| 15/01/2025 | São Paulo     | 30.5                    | 22.0                    | 8.5               | 12.000000         | 78.0                 |
| 15/01/2025 | Rio de Janeiro | 35.0                    | 25.0                    | 10.0              | 11.666667         | 70.0                 |
| 15/01/2025 | Curitiba      | 24.0                    | 18.0                    | 6.0               | 8.000000          | 79.0                 |
| 15/01/2025 | Porto Alegre  | 28.0                    | 20.0                    | 8.0               | 15.000000         | 82.0                 |
| 15/01/2025 | Salvador      | 31.0                    | 24.5                    | 6.5               | 11.666667         | 80.0                 |


````py
# Criando um novo DataFrame contendo apenas as cidades com Temperatura Máxima acima de 30°C
df_high_temp = df[df['Temperatura Máxima (°C)'] > 30]

print("\nDataFrame com cidades com Temperatura Máxima acima de 30°C:\n")
print(df_high_temp)
````


## DataFrame com Cidades com Temperatura Máxima Acima de 30°C:

| Data       | Cidade         | Temperatura Máxima (°C) | Temperatura Mínima (°C) | Amplitude Térmica | Precipitação (mm) | Umidade Relativa (%) |
|------------|---------------|-------------------------|-------------------------|-------------------|-------------------|----------------------|
| 15/01/2025 | São Paulo     | 30.5                    | 22.0                    | 8.5               | 12.000000         | 78.0                 |
| 15/01/2025 | Rio de Janeiro | 35.0                    | 25.0                    | 10.0              | 11.666667         | 70.0                 |
| 15/01/2025 | Salvador      | 31.0                    | 24.5                    | 6.5               | 11.666667         | 80.0                 |
