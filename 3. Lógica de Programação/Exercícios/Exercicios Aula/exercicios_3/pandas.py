df = {}
with open('./cat_breeds.csv', 'r') as arc:
    headers = arc.readline().split(';')
    headers[0] = 'Breed'
    for h in headers:
        df[h] = []
    
    all = arc.readlines()

    for i in range(len(headers)):

        for j in range(len(all)):
            df[headers[i]].append(all[j].split(';')[i])

print(df['Breed'])