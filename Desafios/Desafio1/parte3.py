#%%
# Importar as bibliotecas pandas e matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('googleplaystore.csv')

# Visualizar as primeiras linhas do DataFrame
df.head()

## Análise das Categorias de Apps
# Contar a frequência de cada categoria de aplicativos
category_counts = df['Category'].value_counts()

# Criar o gráfico de pizza
plt.figure(figsize=(14, 8))
plt.subplot(1, 2, 1)  # Definir subtrama para o gráfico de pizza
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Categorias de Apps na Google Play Store')
plt.axis('equal')  # Garantir que o gráfico de pizza seja desenhado como um círculo

# Criar o gráfico de barras
plt.subplot(1, 2, 2)  # Definir subtrama para o gráfico de barras
category_counts.plot(kind='bar', color='skyblue')
plt.title('Contagem de Apps por Categoria na Google Play Store')
plt.xlabel('Categoria')
plt.ylabel('Contagem')
plt.xticks(rotation=90)  # Rotacionar rótulos do eixo x para melhor legibilidade

# Ajustar layout
plt.tight_layout()

# Mostrar os gráficos
plt.show()

