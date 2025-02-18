# Importação das bibliotecas necessárias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# --------------------------------------------
# PASSO 1: Gerar dados fictícios (notas de matemática e ciências)
# --------------------------------------------
np.random.seed(42)  # Define uma semente para garantir que os dados sejam os mesmos toda vez
matematica = np.random.normal(loc=70, scale=15, size=100)  # Notas de matemática (média 70, desvio padrão 15)
ciencias = 0.8 * matematica + np.random.normal(loc=0, scale=10, size=100)  # Notas de ciências correlacionadas com matemática (+ ruído)

# Criar um DataFrame para organizar os dados
dados_alunos = pd.DataFrame({
    'Matematica': matematica,
    'Ciencias': ciencias
})

# --------------------------------------------
# PASSO 2: Padronizar os dados
# --------------------------------------------
# O K-means é sensível à escala dos dados, então padronizamos para média 0 e desvio padrão 1.
scaler = StandardScaler()
dados_padronizados = scaler.fit_transform(dados_alunos)

# --------------------------------------------
# PASSO 3: Método do Cotovelo para encontrar o número ideal de clusters
# --------------------------------------------
# O método do cotovelo ajuda a escolher o número ideal de clusters (K).
# Ele calcula a soma dos quadrados das distâncias dos pontos ao centróide (WCSS) para diferentes valores de K.
# O "cotovelo" no gráfico indica o ponto onde adicionar mais clusters não melhora significativamente o modelo.
wcss = []  # Lista para armazenar os valores de WCSS
for i in range(1, 11):  # Testa K de 1 a 10
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(dados_padronizados)
    wcss.append(kmeans.inertia_)  # inertia_ é o WCSS

# Plotar o gráfico do método do cotovelo
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.xlabel('Número de Clusters (K)')
plt.ylabel('WCSS (Soma dos Quadrados Intra-Cluster)')
plt.title('Método do Cotovelo: Escolha do Número Ideal de Clusters')
plt.grid(True)
plt.show()

# --------------------------------------------
# PASSO 4: Aplicar K-means com o melhor K (baseado no gráfico)
# --------------------------------------------
# Pelo gráfico do cotovelo, escolhemos K=3 (ponto onde a curva "dobra").
k_ideal = 3
kmeans = KMeans(n_clusters=k_ideal, random_state=42)
clusters = kmeans.fit_predict(dados_padronizados)

# Adicionar os clusters ao DataFrame original
dados_alunos['Cluster'] = clusters

# --------------------------------------------
# PASSO 5: Visualizar os clusters
# --------------------------------------------
plt.figure(figsize=(10, 6))
cores = ['blue', 'green', 'orange']  # Cores para cada cluster
rotulos = ['Baixo Desempenho', 'Médio Desempenho', 'Alto Desempenho']  # Legendas claras

# Plotar cada cluster
for i in range(k_ideal):
    cluster = dados_alunos[dados_alunos['Cluster'] == i]
    plt.scatter(cluster['Matematica'], cluster['Ciencias'],
                color=cores[i], label=rotulos[i])

# Plotar os centróides (transformados de volta para a escala original)
centroides = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centroides[:, 0], centroides[:, 1],
            marker='*', s=200, color='red', label='Centróides')

# Configurações do gráfico
plt.xlabel('Nota de Matemática')
plt.ylabel('Nota de Ciências')
plt.title('Agrupamento de Alunos por Desempenho Acadêmico')
plt.legend()
plt.grid(True)
plt.show()

# --------------------------------------------
# PASSO 6: Exibir estatísticas descritivas por cluster
# --------------------------------------------
# Agrupar os dados por cluster e calcular estatísticas descritivas
resumo_clusters = dados_alunos.groupby('Cluster').agg({
    'Matematica': ['count', 'mean', 'std', 'min', 'max'],
    'Ciencias': ['mean', 'std', 'min', 'max']
})

# Renomear as colunas para facilitar a leitura
resumo_clusters.columns = ['Nº Alunos', 'Média Mat', 'Desv. Mat', 'Mín Mat', 'Máx Mat',
                           'Média Cien', 'Desv. Cien', 'Mín Cien', 'Máx Cien']

# Exibir o resumo
print("\n" + "="*65)
print("RESUMO POR CLUSTER:")
print("="*65)
print(resumo_clusters.round(1).to_string(
    formatters={'Nº Alunos': '{:.0f}'.format},
    justify='center',
    index=False
))
print("\nLegenda:")
print("- Alto Desempenho: Notas consistentemente acima da média")
print("- Médio Desempenho: Notas próximas à média")
print("- Baixo Desempenho: Notas abaixo da média, necessitando de reforço")
