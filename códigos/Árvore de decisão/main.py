import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Dados adicionais para permitir mais divisões
dados = {
    'Potência': [70, 90, 120, 150, 100, 130, 110, 170, 140, 160],
    'Peso': [1000, 1200, 1300, 1600, 1100, 1400, 1350, 1800, 1500, 1550],
    'Classe': ['Econômico', 'Econômico', 'Não Econômico', 'Não Econômico', 'Econômico',
               'Não Econômico', 'Econômico', 'Não Econômico', 'Econômico', 'Não Econômico']
}

# Convertendo para DataFrame
df = pd.DataFrame(dados)

# Separando variáveis independentes e dependentes
X = df[['Potência', 'Peso']]
y = df['Classe']

# Criando e treinando a árvore de decisão com parâmetros ajustados para gerar 5 divisões
modelo = DecisionTreeClassifier(criterion='entropy', max_depth=4, min_samples_split=2, min_samples_leaf=1, random_state=42)
modelo.fit(X, y)

# Visualizando a árvore de decisão com 5 divisões
plt.figure(figsize=(12,8))  # Ajustando o tamanho do gráfico para caber melhor a árvore
plot_tree(modelo, feature_names=['Potência', 'Peso'], class_names=['Econômico', 'Não Econômico'], filled=True, rounded=True, proportion=False, fontsize=12)
plt.title("Árvore de Decisão com 5 Divisões", fontsize=14)
plt.show()

# Exibição das regras geradas pela árvore
def exibir_regras(arvore, feature_names, class_names):
    from sklearn.tree import _tree
    tree_ = arvore.tree_
    feature_name = [feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!" for i in tree_.feature]

    def recurse(node, depth):
        indent = "  " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            threshold = tree_.threshold[node]
            # Exibindo a comparação com o threshold (valor de corte) de forma mais clara
            print(f"{indent}- Se {feature_name[node]} <= {threshold:.2f}")
            recurse(tree_.children_left[node], depth + 1)
            print(f"{indent}- Senão (se {feature_name[node]} > {threshold:.2f})")
            recurse(tree_.children_right[node], depth + 1)
        else:
            classe = class_names[np.argmax(tree_.value[node])]
            print(f"{indent}- Classe: {classe}")

    recurse(0, 1)

print("Regras da árvore de decisão:")
exibir_regras(modelo, ['Potência', 'Peso'], ['Econômico', 'Não Econômico'])
