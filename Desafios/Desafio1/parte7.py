#%%
# Importando as bibliotecas pandas e matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo CSV
googleplay_df = pd.read_csv("googleplaystore.csv")

# Remover linhas duplicadas
googleplay_df.drop_duplicates(inplace=True)

# Remover linhas com valores faltantes
googleplay_df.dropna(inplace=True)

# Converter a coluna "Installs" para um tipo numérico
googleplay_df["Installs"] = googleplay_df["Installs"].apply(lambda x: int(x.replace("+", "").replace(",", "")))

# Célula 4: Análise e geração de gráficos
# Gráfico de barras da contagem de aplicativos por categoria
category_counts = googleplay_df["Category"].value_counts().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
category_counts.plot(kind="bar")
plt.title("Contagem de Aplicativos por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Contagem")
plt.xticks(rotation=90)
plt.show()

# Gráfico de dispersão da relação entre avaliação (Rating) e número de instalações (Installs)
plt.figure(figsize=(10, 6))
plt.scatter(googleplay_df["Rating"], googleplay_df["Installs"], alpha=0.5)
plt.title("Relação entre Avaliação e Número de Instalações")
plt.xlabel("Avaliação")
plt.ylabel("Número de Instalações")
plt.show()
