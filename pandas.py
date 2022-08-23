import pandas as pd

df = pd.read_csv("notas_alunos.csv")

media = (df["n1"]+df["n2"])/2
df["media"] = media

if df["faltas"] > 5 or df["media"] < 7:
  df["conceito"] = "Reprovado"
else:
  df["conceito"] = "Aprovado"

df.to_csv('alunos_conceito.csv')

max_num_faltas = df["faltas"].max()
media_total = df["media"].median()
max_media = df["media"].max()

print(f"\nMaior índice de faltas {max_num_faltas}")
print(f"\nMédia total dos alunos {media_total}")
print(f"\nNota máxima {max_media}")