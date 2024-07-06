#%%
# Importando as bibliotecas pandas e matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Célula de Markdown: Carregando e exibindo os primeiros registros do dataset

# Carregar o arquivo CSV
df = pd.read_csv('googleplaystore.csv')

# Exibir os primeiros registros do dataset para entender sua estrutura
print("Primeiros registros do dataset:")
print(df.head())

# Célula de Markdown: Gráfico de barras da distribuição de apps por categoria

# Contagem de apps por categoria
categoria_contagem = df['Category'].value_counts()

# Plotar o gráfico de barras
categoria_contagem.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Distribuição de Apps por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Número de Apps')
plt.xticks(rotation=90)
plt.show()

# Célula de Markdown: Gráfico de dispersão de Rating vs Reviews

# Plotar o gráfico de dispersão Rating vs Reviews
plt.figure(figsize=(10, 6))
plt.scatter(df['Rating'], df['Reviews'], color='green', alpha=0.5)
plt.title('Rating vs Reviews')
plt.xlabel('Rating')
plt.ylabel('Reviews')
plt.show()

# Célula de Markdown: Top 5 apps por menor número de reviews

# Ordenar o dataset pelo número de reviews em ordem crescente
df_sorted_reviews = df.sort_values(by='Reviews')

# Selecionar os top 5 apps com menor número de reviews
top_5_apps_reviews = df_sorted_reviews[['App', 'Reviews']].head()

# Exibir os top 5 apps por menor número de reviews em formato de lista
print("Top 5 apps por menor número de reviews:")
print(top_5_apps_reviews.to_string(index=False))

# Célula de Markdown: O app mais barato existente no dataset

# Converter a coluna de preço para formato numérico
df['Price'] = df['Price'].apply(lambda x: float(x.strip('$')) if '$' in x else 0)

# Selecionar o app mais barato existente no dataset
app_mais_barato = df.loc[df['Price'].idxmin()]

# Exibir o app mais barato existente no dataset
print("\nO app mais barato existente no dataset:")
print(app_mais_barato['App'], "- Preço:", app_mais_barato['Price'])

