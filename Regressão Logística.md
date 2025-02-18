# Criando um gráfico de Regressão Logística

`````py
# Importação das bibliotecas necessárias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Dados simulados: horas de exercício vs risco cardíaco (0 = não, 1 = sim)
data = {
    'horas_exercicio': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 3, 5, 2, 1, 4, 6, 7],
    'risco_cardiaco':  [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0]
}

# Convertendo para DataFrame
heart_data = pd.DataFrame(data)

# Dividindo variáveis independentes (X) e dependente (y)
X = heart_data[['horas_exercicio']]
y = heart_data['risco_cardiaco']

# Dividindo em treino (75%) e teste (25%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Criando e treinando o modelo de regressão logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Fazendo previsões
y_pred_train = model.predict(X_train)  # Previsões para treino
y_pred_test = model.predict(X_test)    # Previsões para teste

# Calculando acurácia
acuracia_treino = accuracy_score(y_train, y_pred_train)
acuracia_teste = accuracy_score(y_test, y_pred_test)

# Resultados
print(f"\nAcurácia nos dados de treino: {acuracia_treino:.2%}")
print(f"Acurácia nos dados de teste: {acuracia_teste:.2%}")
print(f"Coeficiente: {model.coef_[0][0]:.2f} (Impacto das horas de exercício no risco)")
print(f"Intercepto: {model.intercept_[0]:.2f}\n")

# Plotando gráfico da regressão logística
plt.figure(figsize=(10, 6))

# Dados reais
plt.scatter(X, y, color='blue', label='Dados Reais (0 = Sem Risco, 1 = Risco)')

# Curva sigmoide (probabilidade de risco)
x_values = np.linspace(0, 14, 100).reshape(-1, 1)
y_probs = model.predict_proba(x_values)[:, 1]  # Probabilidade de ser classe 1 (risco)
plt.plot(x_values, y_probs, color='red', label='Probabilidade de Risco')

# Linha de decisão (threshold 0.5)
plt.axhline(y=0.5, color='gray', linestyle='--', label='Limiar de Decisão (50%)')

# Configurações do gráfico
plt.xlabel('Horas de Exercício Semanal')
plt.ylabel('Risco Cardíaco / Probabilidade')
plt.title('Regressão Logística: Risco Cardíaco vs Horas de Exercício')
plt.legend()
plt.grid(True)
plt.show()
``````
## Saída Esperada

````text
Acurácia nos dados de treino: 100.00%
Acurácia nos dados de teste: 100.00%
Coeficiente: -1.36 (Impacto das horas de exercício no risco)
Intercepto: 4.93
````
![Gráfico gerado](imagens/grafico4.png)
