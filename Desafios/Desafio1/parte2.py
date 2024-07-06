#%%
# Importando as bibliotecas pandas e matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
df = pd.read_csv('googleplaystore.csv')

# Limpar a coluna 'Installs' removendo caracteres não numéricos
df['Installs'] = df['Installs'].str.replace('[^\d]', '', regex=True)

# Converter a coluna 'Installs' para o tipo numérico
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

# Remover linhas com valores nulos na coluna 'Installs'
df = df.dropna(subset=['Installs'])

# Converter instalações para bilhões e milhões
df['Installs (Billion)'] = df['Installs'] / 1e9
df['Installs (Million)'] = df['Installs'] / 1e6

# Gráfico de barras com os top 5 apps por número de instalação
top_apps = df.nlargest(5, 'Installs')
plt.figure(figsize=(10, 6))
plt.bar(top_apps['App'], top_apps['Installs (Billion)'], color='skyblue')
plt.xlabel('App')
plt.ylabel('Número de Instalações (Bilhões)')
plt.title('Top 5 Apps por Número de Instalação')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()





