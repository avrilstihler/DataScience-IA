# Utilizando a biblioteca Matplotlib para gerar um gráfico de linha
````py
import matplotlib.pyplot as plt

# Definindo os dados
horas = list(range(25))  # Horas do dia (0h a 24h)
temperaturas = [22, 21, 20, 19, 19, 19, 20, 22, 25, 28, 30, 32, 33, 34, 34, 33, 32, 30, 28, 27, 26, 25, 24, 23, 22]

# Criando o gráfico de linha
plt.plot(horas, temperaturas, marker='o', mec="1.0", linestyle='--', color='#FF1493', label='Variação da temperatura')  # Plota os dados com marcadores e linha

# Personalizando o gráfico
plt.title("Evolução da Temperatura em Cerro Azul durante o Dia", fontweight='bold')  # Título do gráfico
plt.xlabel("Hora do Dia")  # Rótulo do eixo X
plt.ylabel("Temperatura (°C)")  # Rótulo do eixo Y
plt.grid(True)  # Adiciona uma grade para facilitar a leitura

# Ajustando os limites dos eixos
plt.xlim(0, 24)  # Define o limite do eixo X (0h a 24h)
plt.ylim(10, 40)  # Define o limite do eixo Y (10°C a 40°C)

# Adicionando rótulos personalizados no eixo X (horas)
plt.xticks(horas)

plt.legend(loc='upper left', fontsize=10)

# Exibindo o gráfico
plt.show()
`````
## Saída Esperada:
![Gráfico Esperado](DataScience-IA/main/imagens/grafico1.png)
