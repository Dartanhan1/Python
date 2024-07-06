#%%
# Importando as bibliotecas pandas e matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("googleplaystore.csv")
# Mostrar o top 10 apps por número de reviews
top_10_apps = df[['App', 'Reviews']].sort_values(by='Reviews', ascending=False).head(10)
top_10_apps
# Plotar um gráfico de barras dos top 10 apps por número de reviews
plt.figure(figsize=(10,6))
plt.barh(top_10_apps['App'], top_10_apps['Reviews'], color='skyblue')
plt.xlabel('Número de Reviews')
plt.ylabel('App')
plt.title('Top 10 Apps por Número de Reviews')
plt.gca().invert_yaxis()  # Inverter o eixo y para exibir o app com mais reviews no topo
plt.show()
