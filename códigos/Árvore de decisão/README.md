# Criando uma Árvore de decisão


## Saída Esperada:

![Gráfico gerado](../../imagens/grafico7.png)

``````text
Regras da árvore de decisão:
  - Se Potência <= 115.00
    - Classe: Econômico
  - Senão (se Potência > 115.00)
    - Se Peso <= 1525.00
      - Se Peso <= 1450.00
        - Classe: Não Econômico
      - Senão (se Peso > 1450.00)
        - Classe: Econômico
    - Senão (se Peso > 1525.00)
      - Classe: Não Econômico
``````
