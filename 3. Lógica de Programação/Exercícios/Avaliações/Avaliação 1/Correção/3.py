months = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'novembro', 'dezembro']

date = input('Data:\n>> ')

invalid = False
if len(date) != 10:
    invalid = True
if date[2] != '/':    
    invalid = True
if date[5] != '/':    
    invalid = True

# 11/06/1977

day = date[:2]
print(day, end=' de ')
month = date[3:5]
month = int(month)
print(months[month-1], end=' de ')

year = date[6:10]

print(year)
