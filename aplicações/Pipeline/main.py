import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error

# 1. Leitura dos dados a partir dos arquivos Excel
train_df = pd.read_excel('car_price_train.xlsx')
test_df = pd.read_excel('car_price_test.xlsx')

# 2. Separando features e target para os dados de treinamento
X_train = train_df.drop('Preco', axis=1)
y_train = train_df['Preco']

# Para os dados de teste, já que não temos a coluna 'Preco'
X_test = test_df.copy()

# 3. Configurando o pré-processamento com ColumnTransformer:
#    - OneHotEncoder para a coluna 'Combustivel'
#    - StandardScaler para as colunas 'Idade' e 'Quilometragem'
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), ['Combustivel']),
        ('num', StandardScaler(), ['Idade', 'Quilometragem'])
    ]
)

# 4. Criando o pipeline com o pré-processamento e o modelo de regressão linear
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# 5. Treinando o modelo com os dados de treinamento
pipeline.fit(X_train, y_train)

# 6. Fazendo previsões
train_pred = pipeline.predict(X_train)
test_pred = pipeline.predict(X_test)

# 7. Avaliando o desempenho nos dados de treinamento (MSE)
mse_train = mean_squared_error(y_train, train_pred)
print(f'MSE nos dados de treinamento: {mse_train:.2f}')

# 8. Criando DataFrames com as previsões

# Previsões para os dados de treinamento: adiciona as colunas Preco Real e Preco Previsto
train_results = X_train.copy()
train_results['Preco Real'] = y_train
train_results['Preco Previsto'] = train_pred

# Previsões para os dados de teste: adiciona a coluna Preco Previsto
test_results = X_test.copy()
test_results['Preco Previsto'] = test_pred

print("\nPrevisões para os dados de treinamento:")
print(train_results)

print("\nPrevisões para os dados de teste:")
print(test_results)

# 9. Plot: Gráfico de regressão linear para os dados de treinamento
# Neste exemplo, vamos plotar Preco Real vs Preco Previsto.
plt.figure(figsize=(8, 6))
plt.scatter(y_train, train_pred, color='blue', label='Dados de Treinamento')
# Linha de referência: y = x (onde o valor previsto seria igual ao valor real)
plt.plot([y_train.min(), y_train.max()], [y_train.min(), y_train.max()], color='red', lw=2, label='Linha de Regressão Ideal')
plt.xlabel('Preço Real')
plt.ylabel('Preço Previsto')
plt.title('Regressão Linear - Dados de Treinamento')
plt.legend()
plt.grid(True)
plt.show()
