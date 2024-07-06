#%%
# Importando as bibliotecas pandas e matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("googleplaystore.csv")

# Remover linhas com valores nulos na coluna 'Price'
df = df.dropna(subset=['Price'])

# Remover caracteres especiais da coluna 'Price' e converter para float
def convert_price(price):
    try:
        return float(price.replace('$', ''))
    except ValueError:
        return None

df['Price'] = df['Price'].apply(convert_price)

# Remover linhas com valores nulos após a conversão
df = df.dropna(subset=['Price'])

# Encontrar o app mais caro
app_mais_caro = df.loc[df['Price'].idxmax()]

print("App mais caro:", app_mais_caro['App'])
print("Preço:", app_mais_caro['Price'])

# Histograma dos preços dos aplicativos
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(df['Price'].mean(), color='red', linestyle='dashed', linewidth=1, label='Preço Médio')
plt.xlabel('Preço ($)')
plt.ylabel('Frequência')
plt.title('Histograma dos Preços dos Aplicativos')
plt.legend()
plt.grid(True)
plt.show()
