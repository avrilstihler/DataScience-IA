# Programa em Python que utiliza uma API de previsão de preços de criptomoedas

````py


````
## Saída Esperada:
````text
Dados recebidos da API CoinGecko (exibindo as 5 primeiras entradas):
[[1708300800000, 51657.0, 52377.0, 51215.0, 52138.0], [1708646400000, 52117.0, 52902.0, 50706.0, 51320.0], [1708992000000, 51295.0, 54925.0, 50598.0, 54478.0], [1709337600000, 54528.0, 63637.0, 54478.0, 62427.0], [1709683200000, 62418.0, 68913.0, 60861.0, 64292.0]]

Dados convertidos para DataFrame:
      Open     High      Low    Close        Data
0  51657.0  52377.0  51215.0  52138.0  2024-02-19
1  52117.0  52902.0  50706.0  51320.0  2024-02-23
2  51295.0  54925.0  50598.0  54478.0  2024-02-27
3  54528.0  63637.0  54478.0  62427.0  2024-03-02
4  62418.0  68913.0  60861.0  64292.0  2024-03-06

Dados salvos no arquivo 'bitcoin_2025.csv'.

DataFrame final com a variável alvo:
      Open     High      Low    Close        Data  Target Movimento
0  51657.0  52377.0  51215.0  52138.0  2024-02-19       0     Baixa
1  52117.0  52902.0  50706.0  51320.0  2024-02-23       1      Alta
2  51295.0  54925.0  50598.0  54478.0  2024-02-27       1      Alta
3  54528.0  63637.0  54478.0  62427.0  2024-03-02       1      Alta
4  62418.0  68913.0  60861.0  64292.0  2024-03-06       1      Alta

Relatório de Classificação:
              precision    recall  f1-score   support

       Baixa       0.24      0.44      0.31         9
        Alta       0.55      0.32      0.40        19

    accuracy                           0.36        28
   macro avg       0.39      0.38      0.35        28
weighted avg       0.45      0.36      0.37        28
````

![Gráfico Esperado](../imagens/grafico9.png)

