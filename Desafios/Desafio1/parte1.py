#%%
# Importando as bibiotecas pandas e matplotlib
import pandas as pd
import matplotlib.pyplot as plt
# Carregar o arquivo CSV
df = pd.read_csv('googleplaystore.csv')

# Visualizar as primeiras linhas do DataFrame
df.head()
# Remover linhas duplicadas
df = df.drop_duplicates()

# Verificar se as linhas duplicadas foram removidas
print("Número de linhas após a remoção de duplicatas:", len(df))
# Salvar o DataFrame modificado em um novo arquivo CSV
df.to_csv('googleplaystore_no_duplicates.csv', index=False)
# Plotar histograma dos ratings dos aplicativos
plt.hist(df['Rating'].dropna(), bins=20, edgecolor='black')
plt.xlabel('Rating')
plt.ylabel('Frequência')
plt.title('Histograma dos Ratings dos Aplicativos')
plt.show()

# %%
