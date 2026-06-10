clean_lines = []
with open('.txt', 'r') as arq:
    for line in arq.readlines():
        clean_line = ''
        for char in line:
            if char.isalpha() or char == ' ':
                clean_line += char
        clean_lines.append(clean_line.title() + '\n')
    
with open('f.txt', 'w') as arq:
    arq.writelines(clean_lines)