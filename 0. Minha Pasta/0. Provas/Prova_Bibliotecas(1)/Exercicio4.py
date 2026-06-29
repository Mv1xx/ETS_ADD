import pandas as pd
import numpy as np

alunos = pd.read_csv("alunos.csv")

print(alunos.head())
print(alunos.columns)
print(alunos.dtypes)
print(alunos.index)

mais10Faltas = alunos[(alunos["faltas"] > 10)]
print(mais10Faltas[['nome', 'faltas']])

ciencia_comp = alunos[(alunos['curso'] == 'Ciência da Computação')]
print(ciencia_comp[['nome', 'curso']])

menos5Faltas = ciencia_comp[(ciencia_comp['faltas'] < 5)]
print(menos5Faltas[['nome', 'curso', 'faltas']])

alunos['cidade'] = alunos['cidade'].fillna('Não Informado')

alunos['nota_prova2'] = alunos['nota_prova2'].fillna(alunos['nota_prova2'].mean())

alunos['média_final'] = alunos['nota_prova1'] + alunos['nota_prova2'] / 2

alunos['Situação_aluno'] = np.where(alunos['média_final'] >= 6, "Aprovado", "Reprovado")

print(alunos[['nome', 'curso', 'Situação_aluno']])

media_curso = alunos.groupby('curso')['média_final'].mean()
print(media_curso)

qntalunos_curso = alunos.groupby('curso')['nome'].count()
print(qntalunos_curso)