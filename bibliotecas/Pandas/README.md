# Utilizando a biblioteca Pandas para criar e modificar um DataFrame
Este código usa Pandas para manipular um DataFrame que contém dados meteorológicos fictícios de cinco cidades brasileiras.
O objetivo principal é explorar funções básicas de um DataFrame em Pandas, demonstrando como criar, modificar e analisar dados.

## Saídas Esperadas:
````
DataFrame original:
````
| Data       | Cidade         | Temperatura Máxima (°C) | Temperatura Mínima (°C) | Precipitação (mm) | Umidade Relativa (%) |
|------------|---------------|-------------------------|-------------------------|-------------------|----------------------|
| 15/01/2025 | São Paulo     | 30.5                    | 22.0                    | 12.0              | 78.0                 |
| 15/01/2025 | Rio de Janeiro | 35.0                   | 25.0                    | NaN               | 70.0                 |
| 15/01/2025 | Curitiba      | 24.0                    | 18.0                    | 8.0               | NaN                  |
| 15/01/2025 | Porto Alegre  | 28.0                    | 20.0                    | 15.0              | 82.0                 |
| 15/01/2025 | Salvador      | 31.0                    | 24.5                    | NaN               | 80.0                 |


````
Verificando valores ausentes:
````

|   | Data  | Cidade | Temperatura Máxima (°C) | Temperatura Mínima (°C) | Precipitação (mm) | Umidade Relativa (%) |
|---|------|--------|-------------------------|-------------------------|-------------------|----------------------|
| 0 | False | False  | False                   | False                   | False             | False               |
| 1 | False | False  | False                   | False                   | True              | False               |
| 2 | False | False  | False                   | False                   | False             | True                |
| 3 | False | False  | False                   | False                   | False             | False               |
| 4 | False | False  | False                   | False                   | True              | False               |


````
Quantidade de valores ausentes por coluna:
````

| Coluna                      | Valores Ausentes |
|-----------------------------|-----------------|
| Data                        | 0               |
| Cidade                      | 0               |
| Temperatura Máxima (°C)     | 0               |
| Temperatura Mínima (°C)     | 0               |
| Precipitação (mm)           | 2               |
| Umidade Relativa (%)        | 1               |

````
Dados após remover linhas com valores ausentes:
````

| Data       | Cidade         | Temperatura Máxima (°C) | Temperatura Mínima (°C) | Precipitação (mm) | Umidade Relativa (%) |
|------------|---------------|-------------------------|-------------------------|-------------------|----------------------|
| 15/01/2025 | São Paulo     | 30.5                    | 22.0                    | 12.000000         | 78.0                 |
| 15/01/2025 | Rio de Janeiro | 35.0                   | 25.0                    | 11.666667         | 70.0                 |
| 15/01/2025 | Porto Alegre  | 28.0                    | 20.0                    | 15.000000         | 82.0                 |
| 15/01/2025 | Salvador      | 31.0                    | 24.5                    | 11.666667         | 80.0                 |


````
Dados após preencher valores ausentes em 'Precipitação' e 'Umidade Relativa':
````

| Data       | Cidade         | Temperatura Máxima (°C) | Temperatura Mínima (°C) | Precipitação (mm) | Umidade Relativa (%) |
|------------|---------------|-------------------------|-------------------------|-------------------|----------------------|
| 15/01/2025 | São Paulo     | 30.5                    | 22.0                    | 12.000000         | 78.0                 |
| 15/01/2025 | Rio de Janeiro | 35.0                   | 25.0                    | 11.666667         | 70.0                 |
| 15/01/2025 | Curitiba      | 24.0                    | 18.0                    | 8.000000          | 79.0                 |
| 15/01/2025 | Porto Alegre  | 28.0                    | 20.0                    | 15.000000         | 82.0                 |
| 15/01/2025 | Salvador      | 31.0                    | 24.5                    | 11.666667         | 80.0                 |


````
Dados com Amplitude Térmica:
````

| Data       | Cidade         | Temperatura Máxima (°C) | Temperatura Mínima (°C) | Precipitação (mm) | Umidade Relativa (%) | Amplitude Térmica |
|------------|---------------|-------------------------|-------------------------|-------------------|----------------------|-------------------|
| 15/01/2025 | São Paulo     | 30.5                    | 22.0                    | 12.000000         | 78.0                 | 8.5               |
| 15/01/2025 | Rio de Janeiro | 35.0                   | 25.0                    | 11.666667         | 70.0                 | 10.0              |
| 15/01/2025 | Curitiba      | 24.0                    | 18.0                    | 8.000000          | 79.0                 | 6.0               |
| 15/01/2025 | Porto Alegre  | 28.0                    | 20.0                    | 15.000000         | 82.0                 | 8.0               |
| 15/01/2025 | Salvador      | 31.0                    | 24.5                    | 11.666667         | 80.0                 | 6.5               |

````
DataFrame Reordenado:
````

| Data       | Cidade         | Temperatura Máxima (°C) | Temperatura Mínima (°C) | Amplitude Térmica | Precipitação (mm) | Umidade Relativa (%) |
|------------|---------------|-------------------------|-------------------------|-------------------|-------------------|----------------------|
| 15/01/2025 | São Paulo     | 30.5                    | 22.0                    | 8.5               | 12.000000         | 78.0                 |
| 15/01/2025 | Rio de Janeiro | 35.0                    | 25.0                    | 10.0              | 11.666667         | 70.0                 |
| 15/01/2025 | Curitiba      | 24.0                    | 18.0                    | 6.0               | 8.000000          | 79.0                 |
| 15/01/2025 | Porto Alegre  | 28.0                    | 20.0                    | 8.0               | 15.000000         | 82.0                 |
| 15/01/2025 | Salvador      | 31.0                    | 24.5                    | 6.5               | 11.666667         | 80.0                 |


````
DataFrame com Cidades com Temperatura Máxima Acima de 30°C:
````

| Data       | Cidade         | Temperatura Máxima (°C) | Temperatura Mínima (°C) | Amplitude Térmica | Precipitação (mm) | Umidade Relativa (%) |
|------------|---------------|-------------------------|-------------------------|-------------------|-------------------|----------------------|
| 15/01/2025 | São Paulo     | 30.5                    | 22.0                    | 8.5               | 12.000000         | 78.0                 |
| 15/01/2025 | Rio de Janeiro | 35.0                    | 25.0                    | 10.0              | 11.666667         | 70.0                 |
| 15/01/2025 | Salvador      | 31.0                    | 24.5                    | 6.5               | 11.666667         | 80.0                 |
