import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Dados fictícios de vendas ao longo de uma semana
dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
vendas = [12000, 15000, 13000, 17000, 20000, 25000, 22000]  # Total de vendas por dia
clientes = [80, 90, 85, 95, 110, 130, 120]  # Número de clientes por dia
lucro = [3000, 4000, 3500, 4500, 5000, 6000, 5500]  # Lucro por dia

# Criando um DataFrame
dados = pd.DataFrame({
    'Dia': dias,
    'Vendas': vendas,
    'Clientes': clientes,
    'Lucro': lucro
})

# Configurações de estilo
sns.set(style="whitegrid")
plt.figure(figsize=(15, 5))

# 1. Gráfico de Barras: Total de Vendas por Dia
plt.subplot(1, 3, 1)
sns.barplot(x='Dia', y='Vendas', data=dados, palette='viridis')
plt.title('Total de Vendas por Dia', fontsize=14, fontweight='bold')
plt.xlabel('Dia da Semana', fontsize=12)
plt.ylabel('Total de Vendas (R$)', fontsize=12)
plt.xticks(rotation=45)

# 2. Gráfico de Dispersão: Número de Clientes vs Total de Vendas
plt.subplot(1, 3, 2)
sns.scatterplot(x='Clientes', y='Vendas', data=dados, s=100, color='#FF69B4', edgecolor='#C71585')
plt.title('Relação entre Clientes e Vendas', fontsize=14, fontweight='bold')
plt.xlabel('Número de Clientes', fontsize=12)
plt.ylabel('Total de Vendas (R$)', fontsize=12)

# 3. Heatmap: Correlação entre Vendas, Clientes e Lucro
plt.subplot(1, 3, 3)
correlacao = dados[['Vendas', 'Clientes', 'Lucro']].corr()
sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlação entre Vendas, Clientes e Lucro', fontsize=14, fontweight='bold')

# Ajustando o layout
plt.tight_layout()
plt.show()
