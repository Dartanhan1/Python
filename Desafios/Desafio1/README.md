# Código completo em Jupyter (.ipynb)

# Etapa 1: Remover as linhas duplicadas:

## Inserir a célula jupyter
**#%%**
## Importando as bibiotecas pandas e matplotlib
import pandas as pd
import matplotlib.pyplot as plt

## Carregar o arquivo CSV
df = pd.read_csv('googleplaystore.csv')

## Visualizar as primeiras linhas do DataFrame
df.head()
## Remover linhas duplicadas
df = df.drop_duplicates()

## Verificar se as linhas duplicadas foram removidas
print("Número de linhas após a remoção de duplicatas:", len(df))
## Salvar o DataFrame modificado em um novo arquivo CSV
df.to_csv('googleplaystore_no_duplicates.csv', index=False)

## Plotar histograma dos ratings dos aplicativos
- plt.hist(df['Rating'].dropna(), bins=20, edgecolor='black')
- plt.xlabel('Rating')
- plt.ylabel('Frequência')
- plt.title('Histograma dos Ratings dos Aplicativos')
- splt.show()

# Etapa 2: Gráfico de barras contendo os top 5 apps por número de instalação:

## Inserir a célula jupyter
#%%
## Importando as bibliotecas pandas e matplotlib
import pandas as pd
import matplotlib.pyplot as plt

## Ler o arquivo CSV
df = pd.read_csv('googleplaystore.csv')

## Limpar a coluna 'Installs' removendo caracteres não numéricos
df['Installs'] = df['Installs'].str.replace('[^\d]', '', regex=True)

## Converter a coluna 'Installs' para o tipo numérico
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

## Remover linhas com valores nulos na coluna 'Installs'
df = df.dropna(subset=['Installs'])

## Converter instalações para bilhões e milhões
- df['Installs (Billion)'] = df['Installs'] / 1e9
- df['Installs (Million)'] = df['Installs'] / 1e6

## Gráfico de barras com os top 5 apps por número de instalação
- top_apps = df.nlargest(5, 'Installs')
- plt.figure(figsize=(10, 6))
- plt.bar(top_apps['App'], top_apps['Installs (Billion)'], color='skyblue')
- plt.xlabel('App')
- plt.ylabel('Número de Instalações (Bilhões)')
- plt.title('Top 5 Apps por Número de Instalação')
- plt.xticks(rotation=45, ha='right')
- plt.tight_layout()
- plt.show()
  
# Etapa 3: Gráfico de pizza (pie chart) mostrando as categorias de apps existentes no dataset de acordo com a frequência em que elas aparecem.

## Inserir a célula jupyter
#%%
## Importar as bibliotecas pandas e matplotlib
import pandas as pd
import matplotlib.pyplot as plt

## Carregar o arquivo CSV
df = pd.read_csv('googleplaystore.csv')

## Visualizar as primeiras linhas do DataFrame
df.head()

## Análise das Categorias de Apps
## Contar a frequência de cada categoria de aplicativos
category_counts = df['Category'].value_counts()

## Criar o gráfico de pizza
- plt.figure(figsize=(14, 8))
- plt.subplot(1, 2, 1)  # Definir subtrama para o gráfico de pizza
- plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
- plt.title('Categorias de Apps na Google Play Store')
- plt.axis('equal')  # Garantir que o gráfico de pizza seja desenhado como um círculo

## Criar o gráfico de barras
- plt.subplot(1, 2, 2)  # Definir subtrama para o gráfico de barras
- category_counts.plot(kind='bar', color='skyblue')
- plt.title('Contagem de Apps por Categoria na Google Play Store')
- plt.xlabel('Categoria')
- plt.ylabel('Contagem')
- plt.xticks(rotation=90)  # Rotacionar rótulos do eixo x para melhor legibilidade

## Ajustar layout
plt.tight_layout()

## Mostrar os gráficos
plt.show()

# Etapa 4: O app mais caro existente no dataset.

## Inserir a célula jupyter
#%%
## Importando as bibliotecas pandas e matplotlib
import pandas as pd
import matplotlib.pyplot as plt

## Carregar os dados
df = pd.read_csv("googleplaystore.csv")

## Remover linhas com valores nulos na coluna 'Price'
df = df.dropna(subset=['Price'])

## Remover caracteres especiais da coluna 'Price' e converter para float
def convert_price(price):
    try:
        return float(price.replace('$', ''))
    except ValueError:
        return None

df['Price'] = df['Price'].apply(convert_price)

## Remover linhas com valores nulos após a conversão
df = df.dropna(subset=['Price'])

## Encontrar o app mais caro
- app_mais_caro = df.loc[df['Price'].idxmax()]

- print("App mais caro:", app_mais_caro['App'])
- print("Preço:", app_mais_caro['Price'])

## Histograma dos preços dos aplicativos
- plt.figure(figsize=(10, 6))
- plt.hist(df['Price'], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
- plt.axvline(df['Price'].mean(), color='red', linestyle='dashed', linewidth=1, label='Preço Médio')
- plt.xlabel('Preço ($)')
- plt.ylabel('Frequência')
- plt.title('Histograma dos Preços dos Aplicativos')
- plt.legend()
- plt.grid(True)
- plt.show()

# Etapa 5: Top 10 apps por número de reviews bem como o respectivo número de reviews. 

## Inserir a célula jupyter
#%%

## Importando as bibliotecas pandas e matplotlib
import pandas as pd
import matplotlib.pyplot as plt

## Carregar os dados
df = pd.read_csv("googleplaystore.csv")
## Mostrar o top 10 apps por número de reviews
- top_10_apps = df[['App', 'Reviews']].sort_values(by='Reviews', ascending=False).head(10)
- top_10_apps

## Plotar um gráfico de barras dos top 10 apps por número de reviews
- plt.figure(figsize=(10,6))
- plt.barh(top_10_apps['App'], top_10_apps['Reviews'], color='skyblue')
- plt.xlabel('Número de Reviews')
- plt.ylabel('App')
- plt.title('Top 10 Apps por Número de Reviews')
- plt.gca().invert_yaxis()  # Inverter o eixo y para exibir o app com mais reviews no topo
- plt.show()

# Etapa 6: Top 5 apps por menor número de reviews e o app mais barato existente no dataset.

## Inserir a célula jupyter
#%%

## Importando as bibliotecas pandas e matplotlib
import pandas as pd
import matplotlib.pyplot as plt

## Célula de Markdown: Carregando e exibindo os primeiros registros do dataset

## Carregar o arquivo CSV
df = pd.read_csv('googleplaystore.csv')

## Exibir os primeiros registros do dataset para entender sua estrutura
- print("Primeiros registros do dataset:")
- print(df.head())

## Célula de Markdown: Gráfico de barras da distribuição de apps por categoria

## Contagem de apps por categoria
categoria_contagem = df['Category'].value_counts()

## Plotar o gráfico de barras
- categoria_contagem.plot(kind='bar', figsize=(10, 6), color='skyblue')
- plt.title('Distribuição de Apps por Categoria')
- plt.xlabel('Categoria')
- plt.ylabel('Número de Apps')
- plt.xticks(rotation=90)
- plt.show()

## Célula de Markdown: Gráfico de dispersão de Rating vs Reviews

## Plotar o gráfico de dispersão Rating vs Reviews
- plt.figure(figsize=(10, 6))
- plt.scatter(df['Rating'], df['Reviews'], color='green', alpha=0.5)
- plt.title('Rating vs Reviews')
- plt.xlabel('Rating')
- plt.ylabel('Reviews')
- plt.show()

## Célula de Markdown: Top 5 apps por menor número de reviews

## Ordenar o dataset pelo número de reviews em ordem crescente
df_sorted_reviews = df.sort_values(by='Reviews')

## Selecionar os top 5 apps com menor número de reviews
top_5_apps_reviews = df_sorted_reviews[['App', 'Reviews']].head()

## Exibir os top 5 apps por menor número de reviews em formato de lista
- print("Top 5 apps por menor número de reviews:")
- print(top_5_apps_reviews.to_string(index=False))

## Célula de Markdown: O app mais barato existente no dataset

## Converter a coluna de preço para formato numérico
df['Price'] = df['Price'].apply(lambda x: float(x.strip('$')) if '$' in x else 0)

## Selecionar o app mais barato existente no dataset
app_mais_barato = df.loc[df['Price'].idxmin()]

## Exibir o app mais barato existente no dataset
- print("\nO app mais barato existente no dataset:")
- print(app_mais_barato['App'], "- Preço:", app_mais_barato['Price'])

# Etapa 7: Duas formas gráficas de exibição dos indicadores acima utilizando a biblioteca matplotlib, escolha os tipos de gráficos linhas e dispersão.

## Inserir a célula jupyter
#%%

## Importando as bibliotecas pandas e matplotlib
import pandas as pd
import matplotlib.pyplot as plt

## Leitura do arquivo CSV
googleplay_df = pd.read_csv("googleplaystore.csv")

## Remover linhas duplicadas
googleplay_df.drop_duplicates(inplace=True)

## Remover linhas com valores faltantes
googleplay_df.dropna(inplace=True)

## Converter a coluna "Installs" para um tipo numérico
googleplay_df["Installs"] = googleplay_df["Installs"].apply(lambda x: int(x.replace("+", "").replace(",", "")))

## Célula 4: Análise e geração de gráficos
## Gráfico de barras da contagem de aplicativos por categoria
- category_counts = googleplay_df["Category"].value_counts().sort_values(ascending=False)
- plt.figure(figsize=(10, 6))
- category_counts.plot(kind="bar")
- plt.title("Contagem de Aplicativos por Categoria")
- plt.xlabel("Categoria")
- plt.ylabel("Contagem")
- plt.xticks(rotation=90)
- plt.show()

## Gráfico de dispersão da relação entre avaliação (Rating) e número de instalações (Installs)
- plt.figure(figsize=(10, 6))
- plt.scatter(googleplay_df["Rating"], googleplay_df["Installs"], alpha=0.5)
- plt.title("Relação entre Avaliação e Número de Instalações")
- plt.xlabel("Avaliação")
- plt.ylabel("Número de Instalações")
- plt.show()
