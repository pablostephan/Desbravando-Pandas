# %%
import pandas as pd

# Criando a Series
dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
series_dados = pd.Series(dados)

# Calculando média, desvio padrão, valor máximo
media = series_dados.mean()
desvio_padrao = series_dados.std()
max_valor = series_dados.max()

print("Média:", media)
print("Desvio Padrão:", desvio_padrao)
print("Máximo Valor:", max_valor)

# %%
import pandas as pd

# Criando o DataFrame
dados = {
    "nome": ["Téo", "Nah", "Napoleão"], 
    "idade": [31, 32, 14]
}
df = pd.DataFrame(dados)

# Sumário de cada coluna
sumario = df.describe()

# Média da coluna idade
media_idade = df["idade"].mean()

# Último nome da coluna nome
ultimo_nome = df["nome"].iloc[-1]

# Exibindo resultados
print("Sumário:\n", sumario)
print("Média da idade:", media_idade)
print("Último nome:", ultimo_nome)
