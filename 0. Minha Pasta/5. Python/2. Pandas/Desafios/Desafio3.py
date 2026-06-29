import pandas as pd

cat = pd.read_csv("../Pandas/CSV/cat_breeds_clean.csv", sep=";")

#A lista de todos os gatos da raça Angora.
angora = (cat[cat['Breed'] == 'Angora'])
print(angora)

#A lista de todos os gatos que moram em países da Europa
europa = cat[(cat['Country'] == 'France') | (cat['Country'] ==  'UK') | (cat['Country'] ==  'Germany')]
print(europa)

#Os países dos gatos laranjas
pais_laranjas = (cat.groupby('Country')['Fur_colour_dominant'].count())
print(pais_laranjas.idxmax(), pais_laranjas[pais_laranjas.idxmax()])

#A razão entre o peso (Kg) e comprimento (m) dos gatos com mais de 6 meses de idade.
meses6 = cat[cat['Age_in_months'] > 6]
meses6['razaodarazaodarazao'] = (meses6["Weight"]) / (meses6['Body_lengt'])
print(meses6)

#A raça, idade e peso de todos os gatos machos.
colunas = ['Breed', 'Age_in_years', 'Weight', 'Gender']
a = cat[colunas]
filtro = a[(a['Gender'] == 'male')]
print(filtro)

#A porcentagem do dia que cada gato Ragdoll passa dormindo 
ragdoll = cat[cat['Breed'] == 'Ragdoll']
ragdoll['Porcentagem_Dormindo_por_dia'] = ragdoll['Sleep_time_hours'] / 24 * 100
print(ragdoll)

#soma do comprimento de todos os gatos
soma_comprimento = cat['Body_lengt'].sum()
print("Soma do comprimento: ", soma_comprimento)

#Média de horas dormidas de todos os gatos
media_horas = cat['Sleep_time_hours'].mean()
print("Média de horas dormidas: ", media_horas)

#O peso total de todos os gatos entre 3 e 12 meses de idade.
friltro2 = cat[(cat['Age_in_months'] > 3) & (cat['Age_in_months'] < 12)]
peso_total = (friltro2['Body_lengt'].sum())
print("Peso Total: ", peso_total)

#A média da razão entre comprimento (cm) e idade dos gatos brancos e pretos da América do Norte
filtro3 = cat[((cat['Fur_colour_dominant'] == 'black') | (cat['Fur_colour_dominant'] == 'white')) & ((cat['Country'] == 'USA') | (cat['Country'] == 'Canada'))]


filtro3['cm_idade'] = (filtro3['Body_lengt'] / filtro3['Age_in_years'])
print(filtro3)
media_razao = filtro3['cm_idade'].mean()
print("Media da razao: ", media_razao)



