# %% 
import pandas as pd    

# Lê o arquivo CSV separado por ";"
df = pd.read_csv("../data/customers.csv", sep=";")
df

# %%
ord = (
    # Ordena por Points (desc) e depois por Name (asc)
    df.sort_values(["Points", "Name"], ascending=[False, True])

      # Renomeia colunas para Id, Nome e Pontos
      .rename(columns={"UUID": "Id", "Name": "Nome", "Points": "Pontos"})

      # Reordena colunas na ordem desejada
      [["Id", "Pontos", "Nome"]]
)

# Exibe o DataFrame final
ord

# %%

# Reordena numa variável as colunas para Id, Nome e Pontos
reord = ord[["Id", "Nome", "Pontos"]]

# Exibe o DataFrame com a nova ordem de colunas
reord
